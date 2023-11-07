from django import forms
from django.forms import Textarea, ModelForm
from .models import User, Board, List, Card


# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ["username", "password"]


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ["name", "description"]


# class ListForm(forms.ModelForm):
#     class Meta:
#         model = List
#         fields = ["name"]


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ["name", "content"]
