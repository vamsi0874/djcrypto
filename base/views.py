# from django.shortcuts import render
from .models import Note
from .serializer import NoteSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializer import UserRegisterSerializer



@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    try:
        print('request:', request.data)
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
    except Exception as e:
        return Response({"error":str(e)}, status=500)


class CustomTokenObtainPairView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        try:
            print('request:', request.data)
            response = super().post(request, *args, **kwargs)
            
            token = response.data
            access_token = token['access']
            refresh_token = token['refresh']
            
            res = Response()
            res.data = {"success":True}

            res.set_cookie(
                key='access_token', value=access_token, 
                httponly=True,
                secure=True,
                samesite='None',
                path='/'
                )
            res.set_cookie(
                key='refresh_token', value=refresh_token, 
                httponly=True,
                secure=True,
                samesite='None',
                path='/'
                )
            return res
        except:
            print("error")
            return Response({"success":False}) 

class CustomRefreshTokenView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        try:
            refesh_token = request.COOKIES.get('refresh_token')
            request.data['refresh'] = refesh_token

            response = super().post(request, *args, **kwargs)
  
            token = response.data
            access_token = token['access']

            res = Response()
            res.data = {"refresh":True}

            res.set_cookie(
                key='access_token', value=access_token, httponly=True,
                secure=True,
                samesite='None',
                path='/'
                )
            return res
        except:
            return Response({"refresh":False})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_notes(request):
    user = request.user
    notes = Note.objects.filter(owner=user)
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def logout(request):
    try:
        res = Response()
        res.data = {"success":True}
        res.delete_cookie('access_token',path='/',samesite='None')
        res.delete_cookie('refresh_token',path='/',samesite='None')
        return res
    except:
        return Response({"success":False})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def is_authenticated(request):
    try:
        return Response({"authenticated":True})  
    except:
        return Response({"authenticated":False})


