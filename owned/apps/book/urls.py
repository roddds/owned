from django.conf.urls import include, url
from book.views import ReadChapter

urlpatterns = [
    url(r'^read/(?P<chapter>[\d]+)/$', ReadChapter.as_view())
]
