from django.conf.urls import patterns, include, url
from book.views import ReadChapter

urlpatterns = patterns('',
    url(r'^read/(?P<chapter>[\d]+)/$', ReadChapter.as_view())
)
