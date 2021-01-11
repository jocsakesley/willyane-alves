
from django.contrib import messages
from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import render, redirect
from .forms import ServiceForm, KitServiceForm
from .models import Service, KitService
from willyanealves.stock.models import Stock
# Create your views here.

def register_service(request):
    form = ServiceForm()
    form_kitservice_factory = inlineformset_factory(Service, KitService, form=KitServiceForm, extra=1)
    form_kitservice = form_kitservice_factory()
    context = {
        'form':form,
        'form_kitservice': form_kitservice
    }
    if request.method == "POST":
        return create_service(request)
    return render(request, "services/register_service.html", context)


def create_service(request):
    form = ServiceForm(request.POST)
    form_kitservice_factory = inlineformset_factory(Service, KitService, form=KitServiceForm)
    form_kitservice = form_kitservice_factory(request.POST, prefix='kitservice')
    context = {
        'form': form,
        'form_kitservice': form_kitservice
    }
    if form.is_valid() and form_kitservice.is_valid():
        s = form.save()
        form_kitservice.instance = s
        form_kitservice.save()
        for ki in KitService.objects.all():
            for s in Stock.objects.all():
                if ki.item.item == s.item and ki.service.service == form.cleaned_data['service']:
                    s.quantity -= ki.quantity
                    s.save()
        #stock.filter(item="Pinça", item_stock__service__service="Maquiagem").annotate(stock=F('quantity')-F('item_stock__quantity')).values_list('stock')
        messages.success(request, "Serviço cadastrado com sucesso", extra_tags="alert-success")
        return render(request, "services/register_service.html", context)

    return render(request, "services/register_service.html", context)


def list_services(request):
    services = Service.objects.prefetch_related('kitservice')
    return render(request, "services/list_services.html", {"services": services })


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
