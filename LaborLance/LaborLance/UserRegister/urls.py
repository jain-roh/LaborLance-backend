
from django.conf.urls import url
from django.contrib import admin
from .views import UserRegisterView,JobSeekerRegisterView,UserRegisterDetailView,JobSeekerRegisterDetailView,BusinessRegisterDetailView,BusinessRegisterView
urlpatterns = [
    url(r'user/$', UserRegisterView.as_view()),
url(r'user/(?P<pk>\d+)/$', UserRegisterDetailView.as_view()),
url(r'jobseeker/$', JobSeekerRegisterView.as_view()),
url(r'jobseeker/(?P<pk>\d+)/$',JobSeekerRegisterDetailView.as_view()),
url(r'business/(?P<pk>\d+)/$',BusinessRegisterDetailView.as_view()),
url(r'business/$', BusinessRegisterView.as_view()),


]
