# from django.shortcuts import render
from django.http import HttpResponse
# from core.models import User
from django.contrib.auth import authenticate
# from django.views.decorators.csrf import csrf_exempt
# from django.http import JsonResponse
from .serializer import UserSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from .serializer import LoginSerializer
from django.contrib.auth import authenticate
from rest_framework.views import APIView

def index(request):

    return HttpResponse("Hello, world. You're at the polls index.")

# @csrf_exempt
@api_view(['POST'])
def register(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        print('data:', data)

        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            user = serializer.save()  # Save user instance
            return Response({'message': 'User created successfully', 'user': serializer.data}, status=201)
        else:
            return Response(serializer.errors, status=400)  # Use DRF Response
    except Exception as e:
        return Response({'error': str(e)}, status=500)  # Use DRF Response
    

@api_view(['POST'])
def login(request):
    
    # print('request:', request.body)
    data = json.loads(request.body.decode('utf-8'))
    serializer = LoginSerializer(data=data)
    
    if serializer.is_valid():
        email = serializer.data['email']
        password = serializer.data['password']

        user = authenticate(email=email, password=password)

        if user is not None:
            return HttpResponse("Login Successful")
        
        else:
            return HttpResponse("Login Failed")
    else:
        return HttpResponse("Invalid Request")



class Login(APIView):
    def post(self , request):

        print('request',request.data)
        
        serializer = LoginSerializer(data=request.data)
        
        if serializer.is_valid():
            email = serializer.data['email']
            password = serializer.data['password']

            print('email',email)
            print('password',password)
    
            user = authenticate(email=email, password=password)
            print('user',user)
    
            if user is not None:
                return HttpResponse("Login Successful")
            
            else:
                return HttpResponse("Login Failed")
        else:
            return HttpResponse("Invalid Request")