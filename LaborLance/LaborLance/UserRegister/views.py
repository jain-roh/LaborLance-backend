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


class UserRegisterDetailView(APIView):
    def get(self, request,pk):
        user = User.objects.get(id=pk)
        data = UserSerializer(user)

        return Response(data.data, status=status.HTTP_200_OK)

class UserRegisterView(APIView):
    serializer_class = UserSerializer
    queryset = UserSerializer(User.objects.all(),many=True)

    def get(self, request):
        user = User.objects.all()
        data = UserSerializer(user, many=True)
        return Response(data.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            # UserRegister.objects.create_user(username==serializer.data)
            user_data=User.objects.create_user(username=serializer.data['username'],password=serializer.data['password'],email=serializer.data['email'],is_staff=serializer.data['is_staff'])
            user_data={'id':user_data.id,'username':user_data.username,'email':user_data.email,'is_staff':user_data.is_staff}
            return Response(user_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobSeekerRegisterDetailView(APIView):
    def get(self, request,pk):
        j = JobSeeker.objects.get(id=pk)
        data = JobSeekerSerializer(j)
        return Response(data.data, status=status.HTTP_200_OK)


class JobSeekerRegisterView(APIView):
    serializer_class = JobSeekerSerializer
    queryset = JobSeeker.objects.all()

    def get(self, request):
        jobseeker=JobSeeker.objects.all()
        data=JobSeekerSerializer(jobseeker,many=True)
        return Response(data.data,status=status.HTTP_200_OK)


    def post(self, request):
        try:
            serializer = JobSeekerSerializer(data=request.data)

            if serializer.is_valid(raise_exception=True):
                serializer.save()
                print('Data',serializer.data.pop('password'))
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print('View Error',e)
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


class BusinessRegisterDetailView(APIView):
    def get(self, request,pk):
        b=Business.objects.get(id=pk)
        data=BusinessSerializer(b)
        return Response(data.data,status=status.HTTP_200_OK)

class BusinessRegisterView(generics.ListCreateAPIView):
    serializer_class = BusinessSerializer
    queryset = Business.objects.all()

    def get(self, request):
        b = Business.objects.all()
        data = BusinessSerializer(b, many=True)
        return Response(data.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BusinessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # UserRegister.objects.create_user(username==serializer.data)
            # User.objects.create_user(username=serializer.data['username'],password=serializer.data['password'],email=serializer.data['email'],is_staff=serializer.data['is_staff'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


