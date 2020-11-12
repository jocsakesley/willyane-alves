from django.shortcuts import render

# Create your views here.
def create_customer_service(request):
    return render(request, "customer_service/create_customer_service.html")