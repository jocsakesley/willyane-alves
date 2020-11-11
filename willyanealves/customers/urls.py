from django.urls import path
from willyanealves.customers.views import register_customer, list_customers, detail_customers, search_customer, delete_customer, update_customer


urlpatterns = [
    path('', register_customer, name='register_customer'),
    path('list/', list_customers, name='list_customers'),
    path('<uuid:new_id>/', detail_customers, name='detail_customers'),
    path('search/', search_customer, name='search_customer'),
    path('delete/<uuid:new_id>/', delete_customer, name='delete_customer'),
    path('update/<uuid:new_id>/', update_customer, name='update_customer'),
]