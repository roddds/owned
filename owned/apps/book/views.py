from django.views.generic.base import TemplateResponseMixin, View
from django.views.generic import DetailView
from book.models import Paragraph
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response


class ParagraphView(TemplateResponseMixin, View):

    model = Paragraph

    def get(self, request, **kwargs):
        chapter = kwargs['chapter']
        import ipdb; ipdb.set_trace()
        paragraph = get_object_or_404(self.model, pk=chapter)
        text = paragraph.text
        return HttpResponse(text)
