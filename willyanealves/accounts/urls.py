from django.contrib import admin
from django.urls import path, include
from willyanealves.accounts.views import login_user, register, logout_user

urlpatterns = [
   path('', login_user, name='login_user'),
   path('register/', register, name='register'),
   path('logout/', logout_user, name='logout_user')
]
