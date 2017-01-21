from django.views.generic import TemplateView
from .models import Paragraph


class BaseBookView(TemplateView):
    def get_context(self):
        cxt = {}
        cxt['url_prefix'] = "/book/read/"
        cxt['paragraph'] = Paragraph.objects.get(pk=self.kwargs['chapter'])
        cxt['options'] = cxt['paragraph'].options.all()
        cxt['player'] = self.request.user
        cxt['saveslot'] = self.request.user.saveslot

        return cxt


class ReadChapter(BaseBookView):
    template_name = 'game/read.html'

    def get(self, request, **kwargs):
        cxt = self.get_context()

        return self.render_to_response(cxt)
