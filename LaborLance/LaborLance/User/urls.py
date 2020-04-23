
from django.conf.urls import url
from django.contrib import admin
from .views import UserRegisterView
urlpatterns = [
    url(r'', UserRegisterView.as_view()),
]
