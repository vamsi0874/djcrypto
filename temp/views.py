from rest_framework.permissions import AllowAny , IsAuthenticated
from django.contrib.auth.models import User
from .models import Note , Coin
from rest_framework import generics
from .serializers import UserSerializer , NoteSerializer , CoinSerializer
from rest_framework.response import Response


class NoteListCreate(generics.ListCreateAPIView):
   
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        print('uuu',user)
        return Note.objects.filter(owner=user)
    
    def perform_create(self, serializer):
        print('serializer:', self.request.user)

        if serializer.is_valid():
            serializer.save(owner=self.request.user)
        else:
            return Response(serializer.errors, status=400)
        
class CoinListCreate(generics.ListCreateAPIView):
   
    serializer_class = CoinSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        print('uuu',user)
        return Coin.objects.filter(owner=user)
    
    def perform_create(self, serializer):
        print('serializer:', self.request.user)

        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
        

class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(owner=user)
    
class CoinDelete(generics.DestroyAPIView):
    serializer_class = CoinSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Coin.objects.filter(owner=user)

class CreateUserView(generics.CreateAPIView):
    
    print('create user')

    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer  

