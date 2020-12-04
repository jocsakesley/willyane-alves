from django.contrib import admin
from datetime import datetime, timedelta
from . import models
# Register your models here.

class ServiceItemInline(admin.TabularInline):
    model = models.ServiceItem
    extra = 1

class ServiceItemAdmin(admin.ModelAdmin):
    list_display = ('customerservice', 'service', 'quantity',)# 'total')

class CustomerServiceAdmin(admin.ModelAdmin):
    model = models.CustomerService
    list_display = ('id','user', 'customer', 'date', 'start', 'discount', ) #'total_service')
    inlines = [
        ServiceItemInline
    ]

    #def total(self, obj):
    #    entries = models.ServiceItem.objects.filter(customerservice=models.CustomerService.objects.get(id=obj.id))
    #    total = 0
    #    for entry in entries:
    #        if models.CustomerService.objects.get(id=obj.id).discount != '':
    #            total += (float(entry.price * entry.quantity) * (1 - (int(models.CustomerService.objects.get(id=obj.id).discount)/100))) * (1 + float(models.CustomerService.objects.get(id=obj.id).payment))
    #        else:
    #            total += float(entry.price * entry.quantity) * (1 + float(models.CustomerService.objects.get(id=obj.id).payment))
#
#        return total
#    total.short_description = 'total'
'''
    def finish(self, obj):
        entries = models.ServiceItem.objects.filter(customerservice=models.CustomerService.objects.get(id=obj.id))
        duration = timedelta()
        for entry in entries:
            (h,m,s) = str(entry.service.duration).split(":")
            duration += timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        finish = datetime.combine(datetime.today(), models.CustomerService.objects.get(id=obj.id).start) + duration

        return finish.time()

    finish.short_description = 'hora de término'
'''
admin.site.register(models.CustomerService, CustomerServiceAdmin)
admin.site.register(models.ServiceItem, ServiceItemAdmin)