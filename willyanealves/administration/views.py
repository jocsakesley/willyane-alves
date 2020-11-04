from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from willyanealves.customers.models import Customer
# Create your views here.
@login_required(login_url='/accounts/')
def dashboard(request):
    customers = Customer.objects.all().count()
    return render(request, 'administration/dashboard.html', {'customers': customers})