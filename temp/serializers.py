from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Note , Coin


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}
 
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at', 'owner']
        extra_kwargs = {'owner': {'read_only': True}}


class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = ['id', 'title', 'content', 'created_at', 'owner']
        extra_kwargs = {'owner': {'read_only': True}}