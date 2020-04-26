from rest_framework import generics
from django.contrib.auth.models import User
from LaborLance.UserRegister.serializer import UserSerializer,JobSeekerSerializer,BusinessSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from rest_framework import status
from LaborLance.InitialMigrations.models import CityState
from .serializer import CityStateSerializer
from rest_framework.response import Response
from django.views import generic


class CityStateViews(APIView):
    def get(self, request):
        cs = CityState.objects.all()
        ser=CityStateSerializer(cs,many=True)
        return Response(ser.data, status=status.HTTP_200_OK)