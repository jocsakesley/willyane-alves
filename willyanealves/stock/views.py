from django.shortcuts import render
from .forms import StockForm
# Create your views here.

def register_stock(request):
    form = StockForm()
    context = {'form': form}
    return render(request, 'stock/register_stock.html', context)
