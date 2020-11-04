from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, redirect
from .forms import CustomersForm
from .models import Customer
from django.db.models import Q, Value
from django.db.models.functions import Concat

def register_customer(request):
    form = CustomersForm()
    if request.method == "POST":
        return create(request)
    return render(request, 'customers/register_customer.html', {'form': form})

def create(request):
    form = CustomersForm(request.POST)
    if not form.is_valid():
        return render(request, 'customers/register_customer.html', {'form': form})
    try:
        Customer.objects.create(name=form.cleaned_data['name'], last_name=form.cleaned_data['last_name'],
                            cpf=form.cleaned_data['cpf'], email=form.cleaned_data['email'], phone=form.cleaned_data['phone'],
                            sex=form.cleaned_data['sex'], address=form.cleaned_data['address'], city=form.cleaned_data['city'],
                            district=form.cleaned_data['district'], birth=form.cleaned_data['birth'])
        messages.success(request, "Cliente cadastrado com sucesso!", extra_tags="alert-success")
    except:
        messages.error(request, "Ocorreu um erro!", extra_tags="alert-danger")
    return render(request, 'customers/register_customer.html', {'form': form})

def list_customers(request):
    customers = Customer.objects.all().order_by("-id")
    return render(request, "customers/list_customers.html", {"customers": customers})

def detail_customers(request, pk):
    try:
        customer_detail = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        raise Http404
    return render(request, "customers/detail_customers.html", {'customer_detail': customer_detail})

def search_customer(request):
    word = request.GET.get("word")
    fields = Concat('name', Value(' '), 'last_name')
    if word:
        customers = Customer.objects.annotate(full_name=fields).filter(Q(full_name__icontains=word) | Q(cpf__icontains=word))
    else:
        customers = Customer.objects.all().order_by('-id')
    return render(request, "customers/search.html", {"customers": customers})

def delete_customer(request, pk):
    try:
        Customer.objects.get(pk=pk).delete()
    except Customer.DoesNotExist:
        messages.info(request, "Cliente não encontrado")
    return redirect('list_customers')

