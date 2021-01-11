from django.contrib import admin
from .models import Kit, KitItem


class KitItemInline(admin.TabularInline):
    model = KitItem
    extra = 1

class KitAdmin(admin.ModelAdmin):
    list_display = ("name",)
    inlines = [KitItemInline]

admin.site.register(Kit, KitAdmin)
admin.site.register(KitItem)
