from django.contrib import admin
from .models import  Estoque


class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('id','estoque','estoqueTerceiros','estoqueProducao','estoqueAvariados','dataInventario')
    list_display_links = ('estoque',)
    #list_filter = ('nome','sobrenome')
    list_per_page = 10
    search_fields = ('estoque',)


admin.site.register(Estoque,EstoqueAdmin)
