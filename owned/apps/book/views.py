from django.views.generic import TemplateView
from .models import Paragraph


class ReadChapter(TemplateView):
    template_name = 'read.html'

    def get_context(self):
        return {
            'url_prefix': "/book/read/",
            'paragraph': Paragraph.objects.get(pk=self.kwargs['chapter']),
            'options': cxt['paragraph'].option_set.all(),
            'player': self.request.user.player,
            'saveslot': self.request.user.player.saveslot,
        }

    def get(self, request, **kwargs):
        context = self.get_context()

        return self.render_to_response(context)
