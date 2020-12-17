<<<<<<< HEAD
from django.urls import path
from .views import create_customer_service, update_customer_service

app_name = "customer_service"

urlpatterns = [
    path('', create_customer_service, name="create"),
    path('update/<int:pk>', update_customer_service, name="update"),
]
=======
from django.urls import path
from .views import create_customer_service, update_customer_service

app_name = "customer_service"

urlpatterns = [
    path('', create_customer_service, name="create"),
    path('update/<int:pk>', update_customer_service, name="update"),
]
>>>>>>> 2deca4933c26dc4dacde616181fe6ac15f0aff64
