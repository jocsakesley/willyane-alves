from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.db.models import Sum, F, FloatField, ExpressionWrapper

from willyanealves.customers.models import Customer
from willyanealves.services.models import Service


class ServiceItemManager(models.Manager):

    def total_time(self):
        return ServiceItem.quantity * ServiceItem.service.duration


class ServiceItem(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    customerservice = models.ForeignKey('CustomerService', on_delete=models.CASCADE, related_name='serviceitem')

    @property
    def total(self):
        total = 0
        subtotal = self.quantity * self.service.price
        if self.customerservice.discount:
            total += float(subtotal) * (1 - (int(self.customerservice.discount) / 100))
        else:
            total += subtotal
        return total

    def __str__(self):
        return self.service.service


class CustomerService(models.Model):
    DISCOUNTS = (
        (0, "0%"),
        (5, "5%"),
        (10, "10%"),
        (15, "15%"),
        (20, "20%"),
    )
    PAYMENTS = (
        ('0', 'À vista'),
        ('0.0239', 'Débito'),
        ('0.0525', '1x'),
        ('0.11', '2x'),
        ('0.1273', '3x'),
    )
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="Usuário")
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, verbose_name="Cliente")
    date = models.DateField("Data")
    start = models.TimeField("Hora de início")
    discount = models.IntegerField("Desconto", blank=True, max_length=2, choices=DISCOUNTS)
    payment = models.CharField("Pagamento", max_length=20, choices=PAYMENTS)

    @property
    def total_service(self):
        total_service = sum([ts[0] for ts in self.serviceitem.annotate(total=ExpressionWrapper(Sum(F('service__price') * F(
            'quantity') * (1 - (F('customerservice__discount') * 1.0 / 100))), output_field=FloatField())).values_list('total')])
        return f"R$ {total_service:.2f}"

    def __str__(self):
        return f'Atendimento {self.pk} em {self.date}'
