from django.conf.urls import patterns, include, url
from core.views import HomeView, LoginView
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view()),
)
