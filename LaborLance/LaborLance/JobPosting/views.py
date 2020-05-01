from rest_framework import generics
from django.contrib.auth.models import User
from LaborLance.UserRegister.serializer import UserSerializer,JobSeekerSerializer,BusinessSerializer
from LaborLance.JobPosting.serializer import JobPostSerializer,JobPostImageSerializer,JobBidSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from.models import JobPost,JobPostImages,JobBid
from rest_framework import status
from rest_framework.response import Response
from django.views import generic
from rest_framework.parsers import FormParser, MultiPartParser


class JobPostDetailView(APIView):
    serializer_class = JobPostSerializer
    queryset = JobPost.objects.all()

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
        # file_obj = request.FILES['file']
        if serializer.is_valid():
            serializer.save()

            # UserRegister.objects.create_user(username==serializer.data)
            # User.objects.create_user(username=serializer.data['username'],password=serializer.data['password'],email=serializer.data['email'],is_staff=serializer.data['is_staff'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JobPostImageDetailView(APIView):
    serializer_class = JobPostSerializer
    queryset = JobPostImages.objects.all()
    parser_classes = (MultiPartParser, FormParser)
    def get(self, request,pk):
        b=JobPostImages.objects.get(id=pk)
        data=JobPostImageSerializer(b)
        return Response(data.data,status=status.HTTP_200_OK)

class JobPostImageView(generics.ListCreateAPIView):
    serializer_class = JobPostImageSerializer
    queryset = JobPostImages.objects.all()
    parser_classes = (MultiPartParser,FormParser)
    def get(self, request):
        b = JobPostImages.objects.all()
        data = JobPostImageSerializer(b, many=True)
        return Response(data.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = JobPostImageSerializer(data=request.data)
        # file_obj = request.FILES['file']
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class JobBidDetailView(APIView):
    serializer_class = JobBidSerializer
    queryset = JobBid.objects.all()

    def get(self, request,pk):
        b=JobBid.objects.get(id=pk)
        data=JobBidSerializer(b)
        return Response(data.data,status=status.HTTP_200_OK)

class JobBidView(generics.ListCreateAPIView):
    serializer_class = JobBidSerializer
    queryset = JobBid.objects.all()

    def get(self, request):
        b = JobBid.objects.all()
        data = JobBidSerializer(b, many=True)
        return Response(data.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = JobBidSerializer(data=request.data)
        # file_obj = request.FILES['file']
        if serializer.is_valid():
            serializer.save()

            # UserRegister.objects.create_user(username==serializer.data)
            # User.objects.create_user(username=serializer.data['username'],password=serializer.data['password'],email=serializer.data['email'],is_staff=serializer.data['is_staff'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

