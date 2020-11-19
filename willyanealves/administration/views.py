from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render
from willyanealves.customers.models import Customer
from willyanealves.customer_service.models import CustomerService, ServiceItem
# Create your views here.

@login_required(login_url='/accounts/')
def dashboard(request):
    customers = Customer.objects.all().count()
    customer_service = CustomerService.objects.all()
    context = {
        'customers': customers,
        'customer_service': customer_service,
    }
    return render(request, 'administration/dashboard.html', context)

