from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from website.forms import RegisterForm, BoardForm, ListForm, CardForm
from website.models import User, Board, List


# Create your views here.


def index(request):
    boards = Board.objects.all()
    context = {
        "boards": boards
    }
    return render(request, "website/home.html", context)


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.set_password(user.password)
            user.save()
            return redirect('home')
    return render(request, "website/register_form.html", {"form": form})


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            return redirect('all_messages')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'website/login.html')


def logout_user(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def create_board(request):
    form = BoardForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            board = form.save(commit=False)
            board.author = request.user
            board.save()
            return redirect("home")
    return render(request, "website/createBoard.html", {"form": form})


@login_required(login_url='login')
def show_board(request, id):
    board = Board.objects.get(id=id)
    return render(request, "website/board.html", {"board": board})


@login_required(login_url='login')
def create_list(request, id):
    form = ListForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            list = form.save(commit=False)
            list.board = Board.objects.get(id=id)
            list.save()
            return redirect("show_board", id)
    return render(request, "website/createList.html", {"form": form})


@login_required(login_url='login')
def show_list(request, id):
    list = List.objects.get(id=id)
    return render(request, "website/list.html", {"list": list})


def create_card(request, id):
    form = CardForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            card = form.save(commit=False)
            card.list = List.objects.get(id=id)
            card.save()
            return redirect("show_list", id)
    return render(request, "website/createCard.html", {"form":form})