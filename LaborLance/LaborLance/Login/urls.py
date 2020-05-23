
from django.conf.urls import url
from django.contrib import admin
from .views import UserLoginDetailView
urlpatterns = [
    url(r'', UserLoginDetailView.as_view()),
]
