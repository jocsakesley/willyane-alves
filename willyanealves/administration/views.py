from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from willyanealves.customers.models import Customer
from willyanealves.customer_service.models import CustomerService, ServiceItem
from .charts import barchart_billing_profit, barchart_customer_service
from datetime import datetime
from .forms import DashForm
# Create your views here.

@login_required(login_url='/accounts/')
def dashboard(request):
    form = DashForm()
    customer_service = CustomerService.objects.prefetch_related('serviceitem')
    customer_service_month = []
    total_billing = 0
    total_profit_month = 0
    date_bp, total, profit = [], [], []
    date_cs, service, qtd = [], [], []
    if request.method == 'POST':
        form = DashForm(request.POST)
        if form.is_valid():
            for cs in customer_service:
                if cs.date.month == int(form.cleaned_data['month']) and cs.date.year == int(form.cleaned_data['year']):
                    total_billing += float(cs.total_service.strip("R$ "))
                    customer_service_month.append(cs)
                    date_bp.append(cs.date)
                    total.append(float(cs.total_service.strip("R$ ")))
                    total_profit_item = 0
                    for si in cs.serviceitem.select_related('service'):
                        total_profit_month += float(si.profit)
                        total_profit_item += float(si.profit)
                        date_cs.append(si.customerservice.date)
                        service.append(si.service.service)
                        qtd.append(si.quantity)
                    profit.append(total_profit_item)
    else:
        for cs in customer_service:
            if cs.date.month == datetime.today().month and cs.date.year == datetime.today().year:
                total_billing += float(cs.total_service.strip("R$ "))
                customer_service_month.append(cs)
                date_bp.append(cs.date)
                total.append(float(cs.total_service.strip("R$ ")))
                total_profit_item = 0
                for si in cs.serviceitem.select_related('service'):
                    total_profit_month += float(si.profit)
                    total_profit_item += float(si.profit)
                    date_cs.append(si.customerservice.date)
                    service.append(si.service.service)
                    qtd.append(si.quantity)
                profit.append(total_profit_item)


    context = {
        'customer_service_month': len(customer_service_month),
        'customer_service': customer_service,
        'barchart': barchart_billing_profit(date_bp, total, profit),
        'barchartcs': barchart_customer_service(date_cs, service, qtd),
        'total_billing': f"{total_billing:.2f}",
        'total_profit': f"{total_profit_month:.2f}",
        'form': form,
    }
    return render(request, 'administration/dashboard.html', context)

