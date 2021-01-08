
from django.db import models
from django.db.models import Sum, F, FloatField
from willyanealves.customers.models import Customer
from willyanealves.stock.models import Stock


class KitItem(models.Model):
    item = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='item_stock')
    quantity = models.PositiveIntegerField("Quantidade")
    service = models.ForeignKey('Service', on_delete=models.CASCADE, related_name='kititem')

    def price(self):
        return self.item.price

    def __str__(self):
        return self.item

class Service(models.Model):

    service = models.CharField("Serviço", max_length=255)
    price = models.DecimalField("Valor", decimal_places=2, max_digits=6)
    duration = models.DurationField("Duração")

    @property
    def cost(self):
        return sum([t[0] for t in self.kititem.annotate(total=Sum(F('item__price')* F('quantity'), output_field=FloatField())).values_list('total')])

    @property
    def profit(self):
        return float(self.price) - self.cost

    def __str__(self):
        return self.service
