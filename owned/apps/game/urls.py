from django.conf.urls import patterns, include, url
from game.views import NewGameView, ContinueGameView, PlayChapterView

urlpatterns = patterns('',
    url(r'^new$', NewGameView.as_view()),
    url(r'^continue$', ContinueGameView.as_view()),
    url(r'^continue/(?P<slot>\d+)', NewGameView.as_view()),

    url(r'^chapter/(?P<chapter>\d+)', PlayChapterView.as_view()),
)