from django.contrib import messages
from django.shortcuts import render
from .forms import ServiceForm
from .models import Service
# Create your views here.
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