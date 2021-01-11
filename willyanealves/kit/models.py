from django.db import models
from willyanealves.stock.models import Stock



class Kit(models.Model):
    name = models.CharField("Nome", max_length=255)

    def __str__(self):
        return self.name


class KitItem(models.Model):
    item = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='kititem')
    quantity = models.PositiveIntegerField("Quantidade")
    kit = models.ForeignKey('Kit', on_delete=models.CASCADE, related_name='kit', null=True)

    def price(self):
        return self.item.price

    def __str__(self):
        return self.item.item
