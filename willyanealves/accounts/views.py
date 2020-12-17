<<<<<<< HEAD
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def login_user(request):
    form = LoginForm()
    if request.method == "POST":
        return login_ok(request)
    else:
        return render(request, 'accounts/login.html', {'form': form})

def login_ok(request):
    username = request.POST['user']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('dashboard')
    else:
        messages.info(request, "Login inválido", extra_tags="alert-danger")
        print(username, password)
        return render(request, 'accounts/login.html', {'form': LoginForm()})

def logout_user(request):
    logout(request)
    return redirect('login_user')


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        return create(request)
    else:
        return render(request, 'accounts/register.html', {'form': form})

def create(request):
    form = RegisterForm(request.POST)
    if not form.is_valid():
        return render(request, 'accounts/register.html', {'form': form})

    if form.cleaned_data['password'] != form.cleaned_data['password2']:
        messages.info(request, "As senhas não correspondem", extra_tags="alert-warning")
        return render(request, 'accounts/register.html', {'form': form})

    if User.objects.filter(username=form.cleaned_data['user']) or User.objects.filter(email=form.cleaned_data['email']):
        messages.info(request, "Usuário ou email já cadastrado", extra_tags="alert-warning")
        return render(request, 'accounts/register.html', {'form': form})

    User.objects.create_user(form.cleaned_data['user'], email=form.cleaned_data['email'], password=form.cleaned_data['password'],
                             first_name=form.cleaned_data['name'], last_name=form.cleaned_data['last_name'])
    messages.success(request, "Usuário criado com sucesso!", extra_tags="alert-success")
    return render(request, 'accounts/register.html', {'form': form})



=======
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def login_user(request):
    form = LoginForm()
    if request.method == "POST":
        return login_ok(request)
    else:
        return render(request, 'accounts/login.html', {'form': form})


def login_ok(request):
    username = request.POST['user']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('dashboard')
    else:
        messages.info(request, "Login inválido", extra_tags="alert-danger")
        print(username, password)
        return render(request, 'accounts/login.html', {'form': LoginForm()})


def logout_user(request):
    logout(request)
    return redirect('login_user')


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        return create(request)
    else:
        return render(request, 'accounts/register.html', {'form': form})


def create(request):
    form = RegisterForm(request.POST)
    if not form.is_valid():
        return render(request, 'accounts/register.html', {'form': form})

    if form.cleaned_data['password'] != form.cleaned_data['password2']:
        messages.info(request, "As senhas não correspondem", extra_tags="alert-warning")
        return render(request, 'accounts/register.html', {'form': form})

    if User.objects.filter(username=form.cleaned_data['user']) or User.objects.filter(email=form.cleaned_data['email']):
        messages.info(request, "Usuário ou email já cadastrado", extra_tags="alert-warning")
        return render(request, 'accounts/register.html', {'form': form})

    User.objects.create_user(
        form.cleaned_data['user'],
        email=form.cleaned_data['email'],
        password=form.cleaned_data['password'],
        first_name=form.cleaned_data['name'],
        last_name=form.cleaned_data['last_name']
    )
    messages.success(request, "Usuário criado com sucesso!", extra_tags="alert-success")
    return render(request, 'accounts/register.html', {'form': form})
>>>>>>> 2deca4933c26dc4dacde616181fe6ac15f0aff64
