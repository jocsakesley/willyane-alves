from django.contrib import admin
from .models import Service
# Register your models here.

class ServiceModelAdmin(admin.ModelAdmin):
    list_display = ("service", "price", "cost", "duration", "profit")
admin.site.register(Service, ServiceModelAdmin)