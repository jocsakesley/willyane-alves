from django.urls import path
from .views import register_stock

urlpatterns = [
    path('', register_stock, name='register_stock'),
]