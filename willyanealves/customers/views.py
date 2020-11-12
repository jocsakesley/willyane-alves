from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from .forms import CustomersForm
from .models import Customer
from django.db.models import Q, Value
from django.db.models.functions import Concat

@login_required(login_url='/accounts/')
def register_customer(request):
    form = CustomersForm()
    if request.method == "POST":
        return create(request)
    return render(request, 'customers/register_customer.html', {'form': form})

@login_required(login_url='/accounts/')
def create(request):
    form = CustomersForm(request.POST, request.FILES)
    if not form.is_valid():
        return render(request, 'customers/register_customer.html', {'form': form})
    try:

        if Customer.objects.filter(cpf=form.cleaned_data['cpf']) and form.cleaned_data['cpf'] != '':
            messages.info(request, "CPF já cadastrado", extra_tags="alert-warning")
            return render(request, 'customers/register_customer.html', {'form': form})
        Customer.objects.create(**form.cleaned_data)
        messages.success(request, "Cliente cadastrado com sucesso!", extra_tags="alert-success")
    except Exception as e:

            messages.error(request, f"Ocorreu um erro! {e}", extra_tags="alert-danger")
    return render(request, 'customers/register_customer.html', {'form': form})

@login_required(login_url='/accounts/')
def list_customers(request):
    customers = Customer.objects.all().order_by("-created_at")
    return render(request, "customers/list_customers.html", {"customers": customers})

@login_required(login_url='/accounts/')
def detail_customers(request, pk):
    try:
        customer_detail = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        raise Http404
    return render(request, "customers/detail_customers.html", {'customer_detail': customer_detail})

@login_required(login_url='/accounts/')
def search_customer(request):
    word = request.GET.get("word")
    fields = Concat('name', Value(' '), 'last_name')
    if word:
        customers = Customer.objects.annotate(full_name=fields).filter(Q(full_name__icontains=word) | Q(cpf__icontains=word))
    else:
        customers = Customer.objects.all().order_by('-created_at')
    return render(request, "customers/search.html", {"customers": customers})

@login_required(login_url='/accounts/')
def delete_customer(request, pk):
    try:
        Customer.objects.get(pk=pk).delete()
    except Customer.DoesNotExist:
        messages.info(request, "Cliente não encontrado")
    return redirect('list_customers')

@login_required(login_url='/accounts/')
def update_customer(request, pk):
    customer = Customer.objects.get(pk=pk)
    if request.method == "POST":
        return update(request, pk)
    else:
        return render(request, "customers/update_customer.html", {"form": CustomersForm(), "customer": customer})

def update(request,pk):
    form = CustomersForm(request.POST, request.FILES)
    customer = Customer.objects.get(pk=pk)

    if not form.is_valid():
        return render(request, "customers/update_customer.html", {"form": form, "customer": customer})

    if Customer.objects.filter(cpf=form.cleaned_data['cpf']) and form.cleaned_data['cpf'] != '' and not Customer.objects.filter(pk=pk):
        messages.info(request, "CPF já cadastrado", extra_tags="alert-warning")
        return render(request, 'customers/update_customer.html', {'form': form})

    customer.name = form.cleaned_data['name']
    customer.last_name = form.cleaned_data['last_name']
    customer.birth = form.cleaned_data['birth']
    customer.cpf = form.cleaned_data['cpf']
    customer.sex = form.cleaned_data['sex']
    customer.email = form.cleaned_data['email']
    customer.phone = form.cleaned_data['phone']
    customer.address = form.cleaned_data['address']
    customer.city = form.cleaned_data['city']
    customer.district = form.cleaned_data['district']
    if customer.picture == '' or form.cleaned_data['picture'] != None:
        customer.picture = form.cleaned_data['picture']
    customer.save()
    messages.success(request, "Informações atualizadas com sucesso!", extra_tags="alert-success")
    return render(request, "customers/update_customer.html", {"form": CustomersForm(), "customer": customer})