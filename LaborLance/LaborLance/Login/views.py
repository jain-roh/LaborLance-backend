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
from ..utility.token_functionality import autheticate_login
from ..UserRegister.serializer import UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics

class UserLoginDetailView(generics.ListCreateAPIView):
    fields = ('username', 'password')
    user = User.objects.all().only(fields)
    serializer_class = UserSerializer

    def get(self, request):
        fields = ('username', 'password')
        user = User.objects.all().only(fields)
        data = UserSerializer
        # token=login(request.data['username'],request.data['password'])
        return Response(status=status.HTTP_200_OK)
    def post(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        token=autheticate_login(request.data['username'],request.data['password'],request,ip)
        print(token)
        if(token):
            print('got token')
            return Response({'authenticated':True,'token':token, 'error':None}, status=status.HTTP_200_OK,headers={})
        else:
            return Response({'authenticated':False,'token':None, 'error':'User not authenticated'},status=status.HTTP_200_OK,headers={})

