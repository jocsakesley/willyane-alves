from django.contrib.auth.decorators import login_required
from django.db.models import Sum, F, FloatField, Count
from django.shortcuts import render
from willyanealves.customer_service.models import CustomerService
from .charts import barchart_billing_profit, barchart_customer_service
from datetime import datetime
from .forms import DashForm


#@login_required(login_url='/accounts/')
def dashboard(request):
    form = DashForm()
    customer_service = CustomerService.objects.prefetch_related('serviceitem')
    if request.method == 'POST':
        form = DashForm(request.POST)
        if form.is_valid():
            date_bp = [dbp[0] for dbp in customer_service.filter(date__month=form.cleaned_data['month'], date__year=form.cleaned_data['year']).values_list('date')]
            total = [tb[0] for tb in customer_service.filter(date__month=form.cleaned_data['month'], date__year=form.cleaned_data['year'])\
                .annotate(total=Sum((F('serviceitem__service__price')*F('serviceitem__quantity'))*(1-(F('serviceitem__customerservice__discount')/100)), output_field=FloatField()))\
                .values_list('total')]
            total_billing = sum(total)
            customer_service_month = customer_service.filter(date__month=form.cleaned_data['month'], date__year=form.cleaned_data['year']).aggregate(Count('id'))['id__count']
            date_cs = [dcs[0] for dcs in customer_service.filter(date__month=form.cleaned_data['month'], date__year=form.cleaned_data['year']).values_list('serviceitem__customerservice__date')]
            profit = [x[0] for x in customer_service.filter(date__month=form.cleaned_data['month'], date__year=form.cleaned_data['year'])\
                .annotate(total=Sum((F('serviceitem__service__price')*F('serviceitem__quantity'))*(1-(F('serviceitem__customerservice__discount')/100))-F('serviceitem__service__cost'),
                                    output_field=FloatField())).values_list('total')]
            total_profit_month = sum(profit)
            service = [s[0] for s in customer_service.filter(date__month=form.cleaned_data['month'], date__year=form.cleaned_data['year']).values_list('serviceitem__service__service')]
            qtd = [q[0] for q in customer_service.filter(date__month=form.cleaned_data['month'], date__year=form.cleaned_data['year']).values_list('serviceitem__quantity')]


    else:
        date_bp = [dbp[0] for dbp in customer_service.filter(date__month=datetime.today().month, date__year=datetime.today().year).values_list('date')]
        total = [tb[0] for tb in customer_service.filter(date__month=datetime.today().month, date__year=datetime.today().year).annotate(total=Sum((F('serviceitem__service__price') * F('serviceitem__quantity')) * (1 - (F('serviceitem__customerservice__discount') / 100)), output_field=FloatField())).values_list('total')]
        total_billing = sum(total)
        customer_service_month = customer_service.filter(date__month=datetime.today().month, date__year=datetime.today().year).aggregate(Count('id'))['id__count']
        date_cs = [dcs[0] for dcs in customer_service.filter(date__month=datetime.today().month, date__year=datetime.today().year).values_list('serviceitem__customerservice__date')]
        profit = [x[0] for x in customer_service.filter(date__month=datetime.today().month, date__year=datetime.today().year).annotate(total=Sum((F('serviceitem__service__price') * F('serviceitem__quantity')) *
            (1 - (F('serviceitem__customerservice__discount') / 100)) - F('serviceitem__service__cost'),output_field=FloatField())).values_list('total')]
        total_profit_month = sum(profit)
        service = [s[0] for s in customer_service.filter(date__month=datetime.today().month, date__year=datetime.today().year).values_list('serviceitem__service__service')]
        qtd = [q[0] for q in customer_service.filter(date__month=datetime.today().month, date__year=datetime.today().year).values_list('serviceitem__quantity')]


    context = {
        'customer_service_month': customer_service_month,
        'customer_service': customer_service,
        'barchart': barchart_billing_profit(date_bp, total, profit),
        'barchartcs': barchart_customer_service(date_cs, service, qtd),
        'total_billing': f"{total_billing:.2f}",
        'total_profit': f"{total_profit_month:.2f}",
        'form': form,
    }
    return render(request, 'administration/dashboard.html', context)

