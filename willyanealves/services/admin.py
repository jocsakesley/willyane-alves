from django.contrib import admin
from .models import Service, KitService
# Register your models here.

class KitServiceInline(admin.TabularInline):
    model = KitService
    extra = 1

class KitServiceAdmin(admin.ModelAdmin):
    list_display = ('kit', 'service')

class ServiceModelAdmin(admin.ModelAdmin):
    list_display = ("service", "price", "cost", "duration", )#"profit")
    inlines = [KitServiceInline]

admin.site.register(Service, ServiceModelAdmin)
admin.site.register(KitService, KitServiceAdmin)
