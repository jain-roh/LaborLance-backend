
from django.conf.urls import url
from django.contrib import admin
from .views import JobPostDetailView,JobPostView
urlpatterns = [
    url(r'post/$', JobPostView.as_view()),
url(r'post/(?P<pk>\d+)/$', JobPostDetailView.as_view()),



]
