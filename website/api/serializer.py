from rest_framework.serializers import ModelSerializer
from website.models import User, Board, List, Card


class BoardSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = ('name', 'description')


class BoardSerializerCreate(ModelSerializer):
    class Meta:
        model = Board
        fields = ('name', 'description', 'author')


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')


class ListSerializerCreate(ModelSerializer):
    class Meta:
        model = List
        fields = ('name', 'board')


class CardSerializer(ModelSerializer):
    class Meta:
        model = Card
        fields = ('name', 'content', 'list')

