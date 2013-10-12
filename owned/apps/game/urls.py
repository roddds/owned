from django.conf.urls import patterns, include, url
from game.views import NewGameView, ContinueGameView, PlayChapterView

urlpatterns = patterns('',
    url(r'^new$', NewGameView.as_view(), name="new-game-select"),
    url(r'^continue$', ContinueGameView.as_view(), name="continue-game-select"),

    url(r'^continue/(?P<chapter>\d+)', PlayChapterView.as_view(), name="play-chapter"),
)