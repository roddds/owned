# -*- coding: utf-8 -*-
from django.views.generic.base import View, TemplateResponseMixin


class HomeView(TemplateResponseMixin, View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        context = {}
        context['title'] = "Owned"
        return self.render_to_response(context)


class GlossaryView(HomeView):
    template_name = "glossario.html"


class HowToView(HomeView):
    template_name = "comojogar.html"


class DownloadView(HomeView):
    template_name = "baixar.html"


class CreditsView(HomeView):
    template_name = "creditos.html"


class ContactView(HomeView):
    template_name = "participe.html"


class ReccommendationsView(HomeView):
    template_name = "recomendacoes.html"


class BlogView(HomeView):
    template_name = "blog.html"


class FAQView(HomeView):
    template_name = "faq.html"
