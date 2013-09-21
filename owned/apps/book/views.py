from django.views.generic import TemplateView
from book.models import Paragraph


class ReadChapter(TemplateView):
    template_name = 'read.html'

    def get_context(self):
        cxt = {}
        cxt['paragraph'] = Paragraph.objects.get(pk=self.kwargs['chapter'])
        cxt['options'] = cxt['paragraph'].option_set.all()

        return cxt

    def get(self, request, **kwargs):
        cxt = self.get_context()
        return self.render_to_response(cxt)


# @render_to('read.html')
# def home(request):
#     p = Paragraph.objects.get(pk=1)
#     return {'paragraph': p,
#             'options': p.option_set.all()}