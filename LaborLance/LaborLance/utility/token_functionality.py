import jwt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from LaborLance.UserRegister.models import Business,JobSeeker
from django.core import serializers
from ..UserRegister.serializer import BusinessSerializer,JobSeekerSerializer

def generate_token(data,secret_key):

    algorithm='HS256'
    encoded_jwt = jwt.encode(data, secret_key, algorithm=algorithm)
    print(encoded_jwt)
    return encoded_jwt

def degenerate_token(token,secret_key):

    algorithm = 'HS256'
    data=jwt.decode(token,secret_key, algorithm=algorithm)
    return data

def autheticate_login(username,password,request):
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request,user)
        print(request.user)
        if user.is_staff:
            data=JobSeeker.objects.get(id=user.id)
            serializer=JobSeekerSerializer(data)
            data=serializer.data
            data.pop('password')
            return generate_token(data),
        else:
            data = Business.objects.get(id=user.id)
            serializer=BusinessSerializer(data)
            data = serializer.data
            data.pop('password')
            return generate_token(data)
def autheticate_login(username,password,request,secret_key):
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request,user)
        print(request.user)
        if user.is_staff:
            data=JobSeeker.objects.get(id=user.id)
            serializer=JobSeekerSerializer(data)
            data=serializer.data
            data.pop('password')
            return generate_token(data,secret_key)
        else:
            data = Business.objects.get(id=user.id)
            serializer=BusinessSerializer(data)
            data = serializer.data
            data.pop('password')
            return generate_token(data,secret_key)
        return None

def authenticate_token(token,secret_key):
    data=degenerate_token(token, secret_key)
    return data