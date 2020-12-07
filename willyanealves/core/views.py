from django.shortcuts import render, redirect


def home(request):
    return redirect('login_user')
