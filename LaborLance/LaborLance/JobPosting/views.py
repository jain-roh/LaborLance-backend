from rest_framework import generics
from django.contrib.auth.models import User
from LaborLance.UserRegister.serializer import UserSerializer,JobSeekerSerializer,BusinessSerializer
from LaborLance.JobPosting.serializer import JobPostSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from.models import JobPost
from rest_framework import status
from rest_framework.response import Response
from django.views import generic


class JobPostDetailView(APIView):
    def get(self, request,pk):
        b=JobPost.objects.get(id=pk)
        data=JobPostSerializer(b)
        return Response(data.data,status=status.HTTP_200_OK)

class JobPostView(generics.ListCreateAPIView):
    serializer_class = JobPostSerializer
    queryset = JobPost.objects.all()

    def get(self, request):
        b = JobPost.objects.all()
        data = JobPostSerializer(b, many=True)
        return Response(data.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = JobPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # UserRegister.objects.create_user(username==serializer.data)
            # User.objects.create_user(username=serializer.data['username'],password=serializer.data['password'],email=serializer.data['email'],is_staff=serializer.data['is_staff'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


