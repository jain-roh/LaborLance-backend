from rest_framework import generics
from django.contrib.auth.models import User
from LaborLance.UserRegister.serializer import UserSerializer,JobSeekerSerializer,BusinessSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from rest_framework import status
from LaborLance.InitialMigrations.models import CityState,Skill
from .serializer import CityStateSerializer
from rest_framework.response import Response
from django.views import generic


class CityStateViews(APIView):
    def get(self, request):
        if request.GET.get('state',None) is None:
            cs = CityState.objects.values('state').distinct()
            # ser=CityStateSerializer(cs,many=True)
            return Response({'items':list(cs)}, status=status.HTTP_200_OK)
        else:
            cs = CityState.objects.filter(state=request.GET.get('state')).values('id','city','state').distinct()
            return Response({'items':list(cs)}, status=status.HTTP_200_OK)

class SkillViews(APIView):
    def get(self, request):
        skill = Skill.objects.filter().values('id','skill')
        return Response({'items':list(skill)}, status=status.HTTP_200_OK)

