from django.shortcuts import render
from rest_framework.decorators import api_view
# Create your views here.
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import UserTable
import hashlib
  
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
        result = hashlib.md5(password.encode())
        hash2 =  result.hexdigest()
        print(hash)
        salt = getCeaserCipher(username,3)
        user  =  UserTable(username=username, password=hash2,salt=salt)
        user.save()
        return HttpResponse("Hello from register")
    except Exception as e:
        print(e)
    


def getCeaserCipher(str,n):
    return ''.join(chr((ord(char) - 97 - n) % 26 + 97) for char in str)