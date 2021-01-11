from django.urls import path
from .views import kit_register

urlpatterns = [
    path('', kit_register, name='kit_register')
]