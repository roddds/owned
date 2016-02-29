from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from lazysignup.decorators import allow_lazy_user
from owned.book.models import Paragraph
from owned.users.models import User

import logging
logger = logging.getLogger("game")


class BaseGameView(TemplateView):
    def get_context(self):
        cxt = {}
        cxt['url_prefix'] = "/game/continue/"
        cxt['paragraph'] = Paragraph.objects.get(pk=self.kwargs['chapter'])
        cxt['player'] = self.request.user
        cxt['slot'] = self.request.user.active_save_slot
        cxt['options'] = [{'choice': x, 'requirements_met': x.requirements_met(cxt['slot'])} for x in cxt['paragraph'].option_set.all()]
        cxt['chapter'] = self.request.user.active_save_slot.current_chapter
        return cxt


class NewGameView(BaseGameView):
    template_name = "new_game.html"

    @method_decorator(allow_lazy_user)
    def get(self, *args, **kwargs):
        cxt = {}

        user = self.request.user

        if not user.is_authenticated():
            return redirect("auth_login")

        if not hasattr(user, 'player'):
            User.setup(user)

        cxt['player'] = self.request.user
        cxt['save_slots'] = cxt['player'].save_slots.ordered()

        return self.render_to_response(cxt)

    def post(self, request, *args, **kwargs):
        selected_slot = int(request.POST['slot'])

        if selected_slot not in (1, 2, 3):
            return HttpResponse(400)

        player = self.request.user.player
        slot = player.save_slots.get_slot(selected_slot)

        slot.new_game()

        logger.debug('Started a new game for player %s on their slot #%d' % (player.username, slot.slot_number))
        return redirect('play-chapter', chapter=slot.current_chapter)


class PlayChapterView(BaseGameView):
    template_name = 'game/read.html'

    def get(self, request, chapter, *args, **kwargs):
        cxt = self.get_context()
        slot = cxt['slot']
        slot.play_chapter(chapter)
        cxt['inventory'] = slot.inventory.all()

        return self.render_to_response(cxt)


class ContinueGameView(BaseGameView):
    @method_decorator(allow_lazy_user)
    def get(self, request, *args, **kwargs):
        user = self.request.user

        if not user.is_authenticated():
            return redirect("auth_login")

        if user.save_slots.count() == 0:
            user.setup()

        if not user.active_save_slot:
            slot = user.save_slots.get_slot(1)
            slot.new_game()

        chapter = user.active_save_slot.current_chapter
        return redirect("game:play-chapter", chapter=chapter)
