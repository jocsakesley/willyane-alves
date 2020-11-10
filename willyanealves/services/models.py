from django.db import models

# Create your models here.
class Service(models.Model):
    service = models.CharField("Serviço", max_length=255)
    price = models.DecimalField("Valor", decimal_places=2, max_digits=6)
    duration = models.DurationField("Duração")
    cost = models.DecimalField("Custo", decimal_places=2, max_digits=6)
    profit = property()

    @property
    def profit(self):
        return self.price - self.cost

    def __str__(self):
        return self.service