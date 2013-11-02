from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from lazysignup.decorators import allow_lazy_user
from book.models import Paragraph
from player.models import Player

import logging
logger = logging.getLogger("game")


class BaseGameView(TemplateView):
    def get_context(self):
        cxt = {}
        cxt['url_prefix'] = "/game/continue/"
        cxt['paragraph'] = Paragraph.objects.get(pk=self.kwargs['chapter'])
        cxt['player'] = self.request.user.player.get()
        cxt['slot'] = self.request.user.player.get().active_save_slot
        cxt['options'] = [{'choice': x, 'requirements_met': x.requirements_met(cxt['slot'])} for x in cxt['paragraph'].option_set.all()]
        cxt['chapter'] = self.request.user.player.get().active_save_slot.current_chapter
        return cxt


class NewGameView(BaseGameView):
    template_name = "new_game.html"

    def get(self, *args, **kwargs):
        cxt = {}

        user = self.request.user

        if not user.is_authenticated():
            return redirect("auth_login")

        if not hasattr(user, 'player'):
            Player.setup(user)

        cxt['player'] = self.request.user.player.get()
        sorted_slots = sorted(cxt['player'].save_slots.all(), key=lambda x: x.index)

        cxt['save_slots'] = sorted_slots
        return self.render_to_response(cxt)

    def post(self, request, *args, **kwargs):
        selected_slot = int(request.POST['slot'])

        if selected_slot not in (1, 2, 3):
            return HttpResponse(400)

        player = self.request.user.player.get()
        slots = [x for x in player.save_slots.all()]
        slot = slots[selected_slot-1]

        if not slot.is_started:
            slot.is_started = True

        slot.set_as_active()
        slot.current_chapter = 1
        slot.inventory.clear()
        slot.events.clear()
        slot.progress.clear()
        slot.save()
        logger.debug('Started a new game for player %s on their slot #%d' % (player.user.username, slot.index))
        return redirect('play-chapter', chapter=slot.current_chapter)


class PlayChapterView(BaseGameView):
    template_name = 'read.html'

    def get(self, request, chapter, *args, **kwargs):
        cxt = self.get_context()
        slot = cxt['slot']
        slot.play_chapter(chapter)
        cxt['inventory'] = slot.inventory.all()

        return self.render_to_response(cxt)


class ContinueGameView(BaseGameView):
    def get(self, request, *args, **kwargs):
        user = self.request.user

        if not user.is_authenticated():
            return redirect("auth_login")

        player = Player.objects.get(user=user)

        chapter = player.active_save_slot.current_chapter
        return redirect("play-chapter", chapter=chapter)
