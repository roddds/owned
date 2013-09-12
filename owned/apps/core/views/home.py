from django.views.generic.base import View, TemplateResponseMixin


class HomeView(TemplateResponseMixin, View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        context = {}
        context['user_authenticated'] = request.user.is_authenticated()
        return self.render_to_response(context)


class LoginView(View):
    def post(self, request, *args, **kwargs):
        context = {}
        import ipdb; ipdb.set_trace()
        return self.render_to_response(context)

