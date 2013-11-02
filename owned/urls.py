from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView, TemplateView
from django.contrib import admin
from lazysignup.views import convert
admin.autodiscover()


urlpatterns = patterns('',

    url(r'^', include('core.urls')),
    url(r'^', include('core.auth_urls')),

    url(r'^convert/$', convert, {'template_name':'convert/convert.html'},
                                name='lazysignup_convert'),
    url(r'^done/$', TemplateView.as_view(template_name='convert/convertion_complete.html'),
                                         name='lazysignup_convert_done'),

    url(r'^book/', include('book.urls')),
    url(r'^game/', include('game.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^new_game$', RedirectView.as_view(url="game/new")),
    url(r'^continue$', RedirectView.as_view(url="game/continue"))

)
