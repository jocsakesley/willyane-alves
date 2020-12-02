from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return redirect('login_user')#render(request, 'index.html')

