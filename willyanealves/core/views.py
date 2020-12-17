<<<<<<< HEAD
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return redirect('login_user')#render(request, 'index.html')

=======
from django.shortcuts import render, redirect


def home(request):
    return redirect('login_user')
>>>>>>> 2deca4933c26dc4dacde616181fe6ac15f0aff64
