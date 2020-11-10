from django.urls import path
from .views import register_service, list_services

urlpatterns = [

    path('', register_service, name="register_service"),
    path('list/', list_services, name="list_services"),
]