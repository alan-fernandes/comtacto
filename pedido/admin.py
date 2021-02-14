from django.contrib import admin
from . import  models


class ItemPedidoInline(admin.TabularInline):
    model = models.Item
    extra = 1


class PedidoAdmin(admin.ModelAdmin):
    inlines = [
        ItemPedidoInline
    ]


admin.site.register(models.Pedido, PedidoAdmin)
admin.site.register(models.Item)