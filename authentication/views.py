from django.shortcuts import render
from rest_framework.decorators import api_view
# Create your views here.
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import UserCustom 
import hashlib
import os
from dotenv import load_dotenv

load_dotenv()
MY_ENV_VAR = os.getenv('PEPPER')

# encoding GeeksforGeeks using md5 hash
# function 

def index(request):
  return HttpResponse("Hello from another app authentication")



@api_view(['POST'])
def register(request):
    try:
        data  =  request.data
        username =  data["username"]
        password = data["password"]
        salt = getCeaserCipher(username,3)
        password_salt_pepper =  password+""+salt+""+MY_ENV_VAR
        result = hashlib.md5(password_salt_pepper.encode())
        hash2 =  result.hexdigest()
        print(hash)
        user  =  UserCustom(username=username, password=hash2,salt=salt)
        user.save()
        return HttpResponse("Hello from register")
    except Exception as e:
        print(e)
    


def getCeaserCipher(str,n):
    return ''.join(chr((ord(char) - 97 - n) % 26 + 97) for char in str)

@api_view(['GET'])
def login(request):
    data =  request.data
    username =  data["username"]
    password =  data["password"]
    salt = getCeaserCipher(username,3)
    password_salt_pepper =  password+""+salt+""+MY_ENV_VAR
    result = hashlib.md5(password_salt_pepper.encode())
    hash2 =  result.hexdigest()
    all_Users =  UserCustom.objects.all()
    listname = []
    for user in all_Users:
        if username==user.username and hash2==user.password:
            return HttpResponse("login successfull")
    
    return HttpResponse("Login Failure")
    
