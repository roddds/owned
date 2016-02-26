from django.conf.urls import include, url
from owned.game.views import NewGameView, ContinueGameView, PlayChapterView

urlpatterns = [
    url(r'^new$', NewGameView.as_view(), name="new-game-select"),
    url(r'^continue$', ContinueGameView.as_view(), name="continue-game-select"),

    url(r'^continue/(?P<chapter>\d+)', PlayChapterView.as_view(), name="play-chapter"),
]
