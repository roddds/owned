from django.conf.urls import url
from owned.book.views import ReadChapter

urlpatterns = [
    url(r'^read/(?P<chapter>[\d]+)/$', ReadChapter.as_view())
]
