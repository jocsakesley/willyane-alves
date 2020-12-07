from django.urls import path
from .views import register_service, list_services, detail_service, delete_service, update_service

urlpatterns = [

    path('', register_service, name="register_service"),
    path('list/', list_services, name="list_services"),
    path('detail/<int:pk>/', detail_service, name="detail_service"),
    path('delete/<int:pk>/', delete_service, name="delete_service"),
    path('update/<int:pk>/', update_service, name="update_service"),
]
