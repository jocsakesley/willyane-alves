from django.contrib import admin
from willyanealves.stock.models import Stock


class StockAdmin(admin.ModelAdmin):
    list_display = ('item', 'price', 'quantity', 'type')


admin.site.register(Stock, StockAdmin)
