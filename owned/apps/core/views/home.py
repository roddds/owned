from django.views.generic.base import View, TemplateResponseMixin


class HomeView(TemplateResponseMixin, View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        context = {}
        context['user_authenticated'] = request.user.is_authenticated()
        context['title'] = "Owned"
        return self.render_to_response(context)
