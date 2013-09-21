from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.contrib import auth


class BaseGameView(TemplateView):
    def get_context(self):
        cxt = {}

class NewGameView(TemplateView):
    template_name = "new_game.html"

    def get(self, *args, **kwargs):
        return self.render_to_response({})


class ContinueGameView(TemplateView):
    pass


class PlayChapterView(TemplateView):
    pass
