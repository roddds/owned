from django.views.generic import TemplateView
from book.models import Paragraph


class BaseBookView(TemplateView):
    def get_context(self):
        cxt = {}
        cxt['paragraph'] = Paragraph.objects.get(pk=self.kwargs['chapter'])
        cxt['options'] = cxt['paragraph'].option_set.all()
        cxt['player'] = self.request.user.player
        cxt['saveslot'] = self.request.user.player.saveslot

        return cxt


class ReadChapter(BaseBookView):
    template_name = 'read.html'

    def get(self, request, **kwargs):
        cxt = self.get_context()


        return self.render_to_response(cxt)
