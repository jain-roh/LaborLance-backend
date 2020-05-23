
from django.conf.urls import url
from django.contrib import admin
from .views import CityStateViews,SkillViews
urlpatterns = [
    url(r'state/$', CityStateViews.as_view()),
    url(r'skill/$', SkillViews.as_view()),
]
