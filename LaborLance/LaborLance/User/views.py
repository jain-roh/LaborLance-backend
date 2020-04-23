from rest_framework import generics
from django.contrib.auth.models import User
from LaborLance.User.serializer import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from rest_framework import status
from rest_framework.response import Response

class UserRegisterView(APIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    def get(self, request):

        return Response('Success is my only mother fucking option',status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            # User.objects.create_user(username==serializer.data)
            User.objects.create_user(username=serializer.data['username'],password=serializer.data['password'],email=serializer.data['email'],is_staff=serializer.data['is_staff'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


