from rest_framework import generics
from django.contrib.auth.models import User
from LaborLance.UserRegister.serializer import UserSerializer,JobSeekerSerializer,BusinessSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from.models import JobSeeker,Business
from rest_framework import status
from rest_framework.response import Response
from django.views import generic


class UserLoginDetailView(APIView):
    def get(self, request,pk):
        user = User.objects.get(id=pk)
        data = UserSerializer(user)
        return Response(data.data, status=status.HTTP_200_OK)




