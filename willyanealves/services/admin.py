
from django.contrib import admin
from .models import Service, KitItem
# Register your models here.

class KitItemInline(admin.TabularInline):
    model = KitItem
    extra = 1

class KitItemAdmin(admin.ModelAdmin):
    list_display = ('item', 'quantity', 'service')

class ServiceModelAdmin(admin.ModelAdmin):
    list_display = ("service", "price", "cost", "duration", )#"profit")
    inlines = [KitItemInline]

admin.site.register(Service, ServiceModelAdmin)
admin.site.register(KitItem, KitItemAdmin)
