from django.contrib import messages
from django.forms import inlineformset_factory
from django.shortcuts import render
from .forms import CustomerServiceForm, ServiceItemForm
from .models import CustomerService, ServiceItem
from django.contrib.auth.models import User
from willyanealves.customers.models import Customer
# Create your views here.


def create_customer_service(request):
    form = CustomerServiceForm()
    users = User.objects.all()
    customers = Customer.objects.all()
    form_serviceitem_factory = inlineformset_factory(CustomerService, ServiceItem, form=ServiceItemForm, extra=1)
    form_serviceitem = form_serviceitem_factory()
    context = {
        'form': form,
        'users': users,
        'customers': customers,
        'form_serviceitem': form_serviceitem,
    }
    if request.method == "POST":
        return create(request)
    return render(request, "customer_service/create_customer_service.html", context)


def create(request):
    form = CustomerServiceForm(request.POST)
    users = User.objects.all()
    customers = Customer.objects.all()
    form_serviceitem_factory = inlineformset_factory(CustomerService, ServiceItem, form=ServiceItemForm)
    form_serviceitem = form_serviceitem_factory(request.POST)
    context = {
        'form': form,
        'users': users,
        'customers': customers,
        'form_serviceitem': form_serviceitem,
    }
    if form.is_valid() and form_serviceitem.is_valid():
        client = form.save()
        form_serviceitem.instance = client
        form_serviceitem.save()
        messages.success(request, "Atendimento registrado com sucesso", extra_tags="alert-success")
        return render(request, "customer_service/create_customer_service.html", context)
    return render(request, "customer_service/create_customer_service.html", context)


