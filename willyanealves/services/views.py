from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, redirect
from .forms import ServiceForm
from .models import Service


def register_service(request):
    form = ServiceForm()
    if request.method == "POST":
        return create_service(request)
    return render(request, "services/register_service.html", {"form": form})


def create_service(request):
    form = ServiceForm(request.POST)
    if not form.is_valid():
        return render(request, "services/register_service.html", {"form": form})
    Service.objects.create(**form.cleaned_data)
    messages.success(request, "Serviço cadastrado com sucesso", extra_tags="alert-success")
    return render(request, "services/register_service.html", {"form": form})


def list_services(request):
    services = Service.objects.all()
    return render(request, "services/list_services.html", {"services": services})


def detail_service(request, pk):
    try:
        service = Service.objects.get(pk=pk)
    except Service.DoesNotExist:
        raise Http404
    return render(request, "services/detail_service.html", {"service": service})


def delete_service(request, pk):
    Service.objects.get(pk=pk).delete()
    return redirect("list_services")


def update_service(request, pk):
    service = Service.objects.get(pk=pk)
    if request.method == "POST":
        return update(request, pk)
    return render(request, "services/update_service.html", {"form": ServiceForm(), "service": service})


def update(request, pk):
    form = ServiceForm(request.POST)
    service = Service.objects.get(pk=pk)
    if not form.is_valid():
        return render(request, "services/update_service.html", {"form": form, "service": service})

    service.service = form.cleaned_data['service']
    service.price = form.cleaned_data['price']
    service.duration = form.cleaned_data['duration']
    service.cost = form.cleaned_data['cost']
    service.save()
    messages.success(request, "Informações salvas com sucesso", extra_tags="alert-success")
    return render(request, "services/update_service.html", {"form": ServiceForm(), "service": service})
