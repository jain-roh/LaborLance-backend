
from django.conf.urls import url
from django.contrib import admin
from .views import UserRegisterView,JobSeekerRegisterView,UserRegisterDetailView,JobSeekerRegisterDetailView,BusinessRegisterDetailView,BusinessRegisterView
urlpatterns = [
    url(r'login/$', UserRegisterView.as_view()),



]
