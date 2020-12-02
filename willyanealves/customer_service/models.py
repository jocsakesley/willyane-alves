from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from willyanealves.customers.models import Customer
from willyanealves.services.models import Service

# Create your models here.

class ServiceItem(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    customerservice = models.ForeignKey('CustomerService', on_delete=models.CASCADE, related_name='serviceitem')

    @property
    def price(self):
        return self.service.price

    @property
    def total(self):
        total = 0
        subtotal = self.quantity * self.price
        if self.customerservice.discount:
            total += float(subtotal) * (1 - (int(self.customerservice.discount) / 100))
        else:
            total += subtotal
        return total

    @property
    def profit(self):
        profit = self.total - float(self.service.cost)
        return profit

    def __str__(self):
        return self.service.service

class CustomerService(models.Model):
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
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="Usuário")
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, verbose_name="Cliente")
    date = models.DateField("Data")
    start = models.TimeField("Hora de início")
    discount = models.CharField("Desconto", blank=True, max_length=2, choices=DISCOUNTS)
    payment = models.CharField("Pagamento", max_length=20, choices=PAYMENTS)

    @property
    def total_service(self):
        total = 0
        for si in self.serviceitem.all():
            total += float(si.total)
        return f"R$ { total:.2f}"

    @property
    def finish(self):
        duration = timedelta()
        for si in self.serviceitem.all():
            (h, m, s) = str(si.service.duration).split(':')
            duration += timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        finish = datetime.combine(datetime.today(), self.start) + duration
        return finish.time()

    def __str__(self):
        return f'Atendimento {self.pk} em {self.date}'
