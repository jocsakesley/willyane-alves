<<<<<<< HEAD

from django.urls import path, include
from .views import dashboard

urlpatterns = [
    path('', dashboard, name='dashboard'),
]
=======
from django.urls import path
from .views import dashboard

urlpatterns = [
    path('', dashboard, name='dashboard'),
]
>>>>>>> 2deca4933c26dc4dacde616181fe6ac15f0aff64
