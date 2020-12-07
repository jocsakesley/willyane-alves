from django.contrib import admin
from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'birth', 'phone', 'cpf', 'email', 'city')


admin.site.register(Customer, CustomerAdmin)
