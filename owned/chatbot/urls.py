from django.conf.urls import url
from owned.chatbot.views import Home

urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),

]
