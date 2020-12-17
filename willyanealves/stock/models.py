from django.db import models
# Create your models here.


class Stock(models.Model):
    TYPES = (
        ("u","Unitário"),
        ("f","Fracionado"),
    )
    item = models.CharField('Item', max_length=255)
    description = models.CharField('Descrição', max_length=255)
    price = models.DecimalField('Valor', decimal_places=2, max_digits=6)
    quantity = models.PositiveIntegerField('Quantidade')
    type = models.CharField("Tipo", choices=TYPES, max_length=1)

    def __str__(self):
        return self.item
