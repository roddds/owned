# -*- coding: utf-8 -*-
from django.views.generic.base import View, TemplateResponseMixin


class HomeView(TemplateResponseMixin, View):
    template_name = 'core/home.html'

    def get(self, request, *args, **kwargs):
        context = {}
        context['title'] = "Owned"
        return self.render_to_response(context)


class GlossaryView(HomeView):
    template_name = "core/glossario.html"


class DownloadView(HomeView):
    template_name = "core/baixar.html"


class CreditsView(HomeView):
    template_name = "core/creditos.html"


class ContactView(HomeView):
    template_name = "core/participe.html"


class ReccommendationsView(HomeView):
    template_name = "core/recomendacoes.html"


class FAQView(HomeView):
    template_name = "core/faq.html"
