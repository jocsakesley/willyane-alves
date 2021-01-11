
from django.db import models
from django.db.models import Sum, F, FloatField
from willyanealves.customers.models import Customer
from willyanealves.stock.models import Stock
from willyanealves.kit.models import Kit


class KitService(models.Model):
    kit = models.ForeignKey(Kit, on_delete=models.CASCADE, related_name='kititem')
    service = models.ForeignKey('Service', on_delete=models.CASCADE, related_name='kitservice')

    def price(self):
        return self.item.price

    def __str__(self):
        return self.kit

class Service(models.Model):
    service = models.CharField("Serviço", max_length=255)
    price = models.DecimalField("Valor", decimal_places=2, max_digits=6)
    duration = models.DurationField("Duração")

    @property
    def cost(self):
        return sum([t[0] for t in self.kitservice.annotate(total=Sum(F('service__price')* F('kit__kit__quantity'), output_field=FloatField())).values_list('total')])

    @property
    def profit(self):
        return float(self.price) - self.cost

    def __str__(self):
        return self.service
