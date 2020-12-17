<<<<<<< HEAD
from django.contrib import admin
from django.urls import path, include
from willyanealves.accounts.views import login_user, register, logout_user

urlpatterns = [
   path('', login_user, name='login_user'),
   path('register/', register, name='register'),
   path('logout/', logout_user, name='logout_user')
]
=======
from django.contrib import admin
from django.urls import path, include
from willyanealves.accounts.views import login_user, register, logout_user

urlpatterns = [
    path('', login_user, name='login_user'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout_user')
]
>>>>>>> 2deca4933c26dc4dacde616181fe6ac15f0aff64
