from django.conf.urls import url
from owned.core.views import (HomeView,
                              GlossaryView,
                              DownloadView,
                              CreditsView,
                              ContactView,
                              ReccommendationsView,
                              FAQView)

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^glossary$', GlossaryView.as_view(), name='glossary'),
    url(r'^download$', DownloadView.as_view(), name='download'),
    url(r'^credits$', CreditsView.as_view(), name='credits'),
    url(r'^contact$', ContactView.as_view(), name='contact'),
    url(r'^recommendations$', ReccommendationsView.as_view(), name='recommendations'),
    url(r'^faq$', FAQView.as_view(), name='faq'),
]
