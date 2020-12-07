from django.contrib import admin
from .models import Service


class ServiceModelAdmin(admin.ModelAdmin):
    list_display = ("service", "price", "cost", "duration", "profit")


admin.site.register(Service, ServiceModelAdmin)
