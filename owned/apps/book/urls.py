from django.conf.urls import patterns, include, url
from book.views import ParagraphView

urlpatterns = patterns('',
    url(r'^read/(?P<chapter>[\d]+)/$', ParagraphView.as_view())
)
