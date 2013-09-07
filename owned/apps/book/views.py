from django.views.generic import TemplateView
from book.models import Paragraph


class ReadChapter(TemplateView):
    template_name = 'read.html'

    def get_base_context(self):
        cxt = {}
        paragraph = Paragraph.objects.get(pk=self.kwargs['chapter'])
        options = paragraph.option_set.all()
        cxt['paragraph'] = paragraph
        cxt['options'] = options

        return cxt

    def get(self, request, **kwargs):
        cxt = self.get_base_context()
        return self.render_to_response(cxt)


# @render_to('read.html')
# def home(request):
#     p = Paragraph.objects.get(pk=1)
#     return {'paragraph': p,
#             'options': p.option_set.all()}