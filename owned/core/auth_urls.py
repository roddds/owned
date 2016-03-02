#! -*- coding: utf-8 -*-
"""
Urls de autenticação do Owned

* Login do usuário: login/
* Logout do usuário: logout/

* Alteração de senha em: password/alterar/
* Reset da senha em: password/reset/


"""

from django.conf.urls import url

from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

from registration.backends.default.views import ActivationView
from registration.backends.default.views import RegistrationView
from registration.forms import RegistrationFormUniqueEmail


class RegistrationViewUniqueEmail(RegistrationView):
    form_class = RegistrationFormUniqueEmail


urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}, name='auth_login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'registration/logout.html'}, name='auth_logout'),

    url(r'^password/change/done/?', auth_views.password_change_done, name='auth_password_change_done'),
    url(r'^password/change/?', auth_views.password_change, name='auth_password_change'),

    url(r'^password/reset/$', auth_views.password_reset, name='auth_password_reset'),
    url(r'^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.password_reset_confirm, name='auth_password_reset_confirm'),
    url(r'^password/reset/complete/$', auth_views.password_reset_complete, name='auth_password_reset_complete'),
    url(r'^password/reset/done/$', auth_views.password_reset_done, name='auth_password_reset_done'),

    url(r'^ativar/complete/$', TemplateView.as_view(template_name='registration/activation_complete.html'), name='registration_activation_complete'),
    url(r'^ativar/(?P<activation_key>\w+)/$', ActivationView.as_view(), name='registration_activate'),
    # Activation keys get matched by \w+ instead of the more specific
    # [a-fA-F0-9]{40} because a bad activation key should still get to the view;
    # that way it can return a sensible "invalid key" message instead of a
    # confusing 404.
    url(r'^registro/$', RegistrationViewUniqueEmail.as_view(), name='registration_register'),
    url(r'^registro/complete/$', TemplateView.as_view(template_name='registration/registration_complete.html'), name='registration_complete'),
    url(r'^registro/closed/$', TemplateView.as_view(template_name='registration/registration_closed.html'), name='registration_disallowed'),
    # (r'', include('registration.auth_urls')),
]
