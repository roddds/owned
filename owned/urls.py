from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^', include('core.urls')),
    # url(r'game/$', include('game.urls')),
    url(r'^book/', include('book.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
