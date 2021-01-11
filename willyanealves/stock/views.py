from django.shortcuts import render
from .forms import StockForm
from .models import Stock
# Create your views here.

def register_stock(request):
    form = StockForm()
    context = {'form': form}
    if request.method == "POST":
        return create(request)
    return render(request, 'stock/register_stock.html', context)

def create(request):
    form = StockForm(request.POST)
    context = {'form': form}
    if form.is_valid():
        form.save()
        return render(request, 'stock/register_stock.html', context)
    return render(request, 'stock/register_stock.html', context)