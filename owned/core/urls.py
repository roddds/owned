from django.conf.urls import url
from core.views import (HomeView,
                        GlossaryView,
                        HowToView,
                        DownloadView,
                        CreditsView,
                        ContactView,
                        ReccommendationsView,
                        BlogView,
                        FAQView)

urlpatterns = [
    url(r'^$', HomeView.as_view()),

    url(r'^halp$', GlossaryView.as_view()),
    url(r'^howto$', HowToView.as_view()),
    url(r'^piratebay$', DownloadView.as_view()),
    url(r'^whodunit$', CreditsView.as_view()),
    url(r'^enlarge_your_penis$', ContactView.as_view()),
    url(r'^recs$', ReccommendationsView.as_view()),
    url(r'^blog$', BlogView.as_view()),
    url(r'^faq$', FAQView.as_view()),
]