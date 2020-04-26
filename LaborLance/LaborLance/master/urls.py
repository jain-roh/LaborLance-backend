
from django.conf.urls import url
from django.contrib import admin
from .views import CityStateViews
urlpatterns = [
    url(r'citystate/$', CityStateViews.as_view()),
]
