<<<<<<< HEAD
from django.contrib import admin
from .models import Customer
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'birth', 'phone', 'cpf', 'email', 'city')

admin.site.register(Customer, CustomerAdmin)
=======
from django.contrib import admin
from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'birth', 'phone', 'cpf', 'email', 'city')


admin.site.register(Customer, CustomerAdmin)
>>>>>>> 2deca4933c26dc4dacde616181fe6ac15f0aff64
