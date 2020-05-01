import jwt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate



def generate_token(data):
    secret='my_secret'
    algorithm='HS256'
    encoded_jwt = jwt.encode(data, secret, algorithm=algorithm)
    return encoded_jwt

def degenerate_token(token):
    secret = 'my_secret'
    algorithm = 'HS256'
    data=jwt.decode(token,secret, algorithm=algorithm)
    return data
# def login(username,password):
#     user = authenticate(username='john', password='secret')
#     if user is not None:
