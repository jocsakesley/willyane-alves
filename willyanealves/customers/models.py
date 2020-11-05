from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField("Nome", max_length=255)
    last_name = models.CharField("Sobrenome", max_length=255)
    cpf = models.CharField("CPF", max_length=14, unique=True, blank=True)
    email = models.EmailField("Email", max_length=255)
    phone = models.CharField("Telefone", max_length=14)
    sex = models.CharField("Sexo", max_length=10)
    address = models.CharField("Endereço", max_length=255, blank=True)
    city = models.CharField("Cidade", max_length=255)
    district = models.CharField("Bairro", max_length=255, blank=True)
    birth = models.DateField("Data de nascimento", max_length=10, blank=True)

    def __str__(self):
        return self.name