from django.contrib import messages
from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import render, redirect
from .forms import ServiceForm, KitItemForm
from .models import Service, KitItem
from willyanealves.stock.models import Stock
# Create your views here.

def register_service(request):
    form = ServiceForm()
    form_kititem_factory = inlineformset_factory(Service, KitItem, form=KitItemForm, extra=1)
    form_kititem = form_kititem_factory()
    context = {
        'form':form,
        'form_kititem': form_kititem
    }
    if request.method == "POST":
        return create_service(request)
    return render(request, "services/register_service.html", context)


def create_service(request):
    form = ServiceForm(request.POST)
    form_kititem_factory = inlineformset_factory(Service, KitItem, form=KitItemForm)
    form_kititem = form_kititem_factory(request.POST, prefix='kititem')
    context = {
        'form': form,
        'form_kititem': form_kititem
    }
    if form.is_valid() and form_kititem.is_valid():
        s = form.save()
        form_kititem.instance = s
        form_kititem.save()
        for ki in KitItem.objects.all():
            for s in Stock.objects.all():
                if ki.item.item == s.item and ki.service.service == form.cleaned_data['service']:
                    s.quantity -= ki.quantity
                    s.save()
        #stock.filter(item="Pinça", item_stock__service__service="Maquiagem").annotate(stock=F('quantity')-F('item_stock__quantity')).values_list('stock')
        messages.success(request, "Serviço cadastrado com sucesso", extra_tags="alert-success")
        return render(request, "services/register_service.html", context)

    return render(request, "services/register_service.html", context)


def list_services(request):
    services = Service.objects.prefetch_related('kititem')


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
