from django.contrib import admin
from datetime import datetime, timedelta
from . import models


class ServiceItemInline(admin.TabularInline):
    model = models.ServiceItem
    extra = 1


class ServiceItemAdmin(admin.ModelAdmin):
    list_display = ('customerservice', 'service', 'quantity')


class CustomerServiceAdmin(admin.ModelAdmin):
    model = models.CustomerService
    list_display = ('id', 'user', 'customer', 'date', 'start', 'discount')
    inlines = [ServiceItemInline]


admin.site.register(models.CustomerService, CustomerServiceAdmin)
admin.site.register(models.ServiceItem, ServiceItemAdmin)
