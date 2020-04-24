from rest_framework import generics
from django.contrib.auth.models import User
from LaborLance.UserRegister.serializer import UserSerializer,JobSeekerSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from.models import JobSeeker
from rest_framework import status
from rest_framework.response import Response
from django.views import generic


class UserRegisterDetailView(APIView):
    def get(self, request,pk):
        user = User.objects.get(id=pk)
        data = UserSerializer(user)
        return Response(data.data, status=status.HTTP_200_OK)

class UserRegisterView(APIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get(self, request):
        # user = User.objects.get(id=pk)
        # data = UserSerializer.serialize(user)
        # return Response(data.data, status=status.HTTP_200_OK)
        user = User.objects.all()
        data = UserSerializer(user, many=True)
        return Response(data.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            # UserRegister.objects.create_user(username==serializer.data)
            User.objects.create_user(username=serializer.data['username'],password=serializer.data['password'],email=serializer.data['email'],is_staff=serializer.data['is_staff'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobSeekerRegisterView(APIView):
    serializer_class = JobSeekerSerializer
    queryset = JobSeeker.objects.all()

    def get(self, request):
        jobseeker=JobSeeker.objects.all()
        data=JobSeekerSerializer(jobseeker,many=True)
        return Response(data.data,status=status.HTTP_200_OK)


    def post(self, request):
        serializer = JobSeekerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JobSeekerRegisterDetailView(APIView):
    def get(self, request,pk):
        jobseeker=JobSeeker.objects.get(id=pk)
        data=JobSeekerSerializer(jobseeker)
        return Response(data.data,status=status.HTTP_200_OK)


class BusinessRegisterView(APIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get(self, request):
        # user = User.objects.get(id=pk)
        # data = UserSerializer.serialize(user)
        # return Response(data.data, status=status.HTTP_200_OK)
        user = User.objects.all()
        data = UserSerializer(user, many=True)
        return Response(data.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            # UserRegister.objects.create_user(username==serializer.data)
            User.objects.create_user(username=serializer.data['username'],password=serializer.data['password'],email=serializer.data['email'],is_staff=serializer.data['is_staff'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


