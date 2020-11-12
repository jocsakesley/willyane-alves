from django.db import models
import uuid


class Customer(models.Model):
    new_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Nome", max_length=255)
    last_name = models.CharField("Sobrenome", max_length=255)
    cpf = models.CharField("CPF", max_length=14, blank=True, null=True)
    email = models.EmailField("Email", max_length=255)
    phone = models.CharField("Telefone", max_length=14)
    sex = models.CharField("Sexo", max_length=10)
    address = models.CharField("Endereço", max_length=255, blank=True)
    city = models.CharField("Cidade", max_length=255)
    district = models.CharField("Bairro", max_length=255, blank=True)
    birth = models.DateField("Data de nascimento", max_length=10, blank=True, null=True)
    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    modified_at = models.DateTimeField("Modificado em", auto_now=True)
    picture = models.ImageField("Foto", blank=True, upload_to='pictures/%Y/%m/', default='default.png', null=True)

    def __str__(self):
        return self.name