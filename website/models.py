from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    USERNAME_FIELD = 'username'


class Board(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class List(models.Model):
    name = models.CharField(max_length=100)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)


class Card(models.Model):
    name = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    list = models.ForeignKey(List, on_delete=models.CASCADE)
