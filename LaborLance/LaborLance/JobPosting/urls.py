
from django.conf.urls import url
from django.contrib import admin
from .views import JobPostDetailView,JobPostView,JobPostImageView,JobPostImageDetailView,JobBidDetailView,JobBidView
urlpatterns = [
    url(r'post/$', JobPostView.as_view()),
url(r'post/(?P<pk>\d+)/$', JobPostDetailView.as_view()),
url(r'post/image/$', JobPostImageView.as_view()),
url(r'post/image/(?P<pk>\d+)/$', JobPostImageDetailView.as_view()),
    url(r'bid/$', JobBidView.as_view()),
    url(r'bid/(?P<pk>\d+)/$', JobBidDetailView.as_view()),


]
