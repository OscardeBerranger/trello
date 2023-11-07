from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from website.api.serializer import *
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import api_view, permission_classes


# Create your views here.


@api_view(['GET'])
def index(request):
    boards = Board.objects.all()
    serialized_boards = BoardSerializer(boards, many=True)
    return Response(serialized_boards.data)


@api_view(['POST'])
def register(request):
    if request.method == "POST":
        user = RegisterSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return Response(user.data,
                            status=status.HTTP_201_CREATED)  # Si ici je me user.data.username une erreure apparait
    return Response("Something didn't worked out", status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_board(request):
    board = BoardSerializerCreate(data=request.data)
    if board.is_valid():
        board.save()
        return Response(board.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def show_board(request, id):
    board = get_object_or_404(Board, id=id)
    board = BoardSerializer(board)
    return Response(board.data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_list(request):
    list = ListSerializerCreate(data=request.data)
    if list.is_valid():
        list.save()
        return Response(list.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def show_list(request, id):
    list = get_object_or_404(List, id=id)
    list = ListSerializerCreate(list)
    return Response(list.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_list(request, id):
    List.objects.filter(id=id).delete()
    return Response("you just deleted a list", status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_card(request):
    card = CardSerializer(data=request.data)
    if card.is_valid():
        return Response(card.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def show_card(request, id):
    card = get_object_or_404(Card, id=id)
    card = CardSerializer(card)
    return Response(card.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_card(request, id):
    Card.objects.filter(id=id).delete()
    return Response("you just deleted a card", status=status.HTTP_200_OK)
