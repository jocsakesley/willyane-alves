from django import forms
from django.contrib.auth.models import User
from willyanealves.customers.models import Customer
from .models import ServiceItem, CustomerService
class CustomerServiceForm(forms.ModelForm):
    DISCOUNTS = (
        ('0', "0%"),
        ('5', "5%"),
        ('10', "10%"),
        ('15', "15%"),
        ('20', "20%"),
    )
    PAYMENTS = (
        ('0', 'À vista'),
        ('0.0239', 'Débito'),
        ('0.0525', '1x'),
        ('0.11', '2x'),
        ('0.1273', '3x'),
    )
    #user = forms.ModelChoiceField(label='Usuário', queryset=User.objects.all())
    #customer = forms.ModelChoiceField(label='Cliente', queryset=Customer.objects.all())
    date = forms.DateField(label="Data",)
    start = forms.TimeField(label="Hora de início")
    #finish = forms.TimeField(label="Hora de término", required=False)
    discount = forms.CharField(label="Desconto", required=False, widget=forms.Select(choices=DISCOUNTS))
    payment = forms.CharField(label="Pagamento", widget=forms.Select(choices=PAYMENTS))
    #total = forms.FloatField(label="Total", required=False)
    class Meta:
        model = CustomerService
        exclude =['created_at', 'modified_at']

class ServiceItemForm(forms.ModelForm):
    class Meta:
        model = ServiceItem
        fields = '__all__'

