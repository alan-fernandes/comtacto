from django.contrib import admin
from .models import  *


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id','codigo','nome','fornecedor','status')
    list_display_links = ('codigo','nome')
    list_per_page = 10
    search_fields = ('codigo','nome',)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links = ('nome',)
    list_per_page = 10
    search_fields = ('nome',)

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links = ('nome',)
    list_per_page = 10
    search_fields = ('nome',)

class TipoAdmin(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links = ('nome',)
    list_per_page = 10
    search_fields = ('nome',)

class DivisaoAdmin(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links = ('nome',)
    list_per_page = 10
    search_fields = ('nome',)

class MarcaAdmin(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links = ('nome',)
    list_per_page = 10
    search_fields = ('nome',)

class NcmAdmin(admin.ModelAdmin):
    list_display = ('id','codigo','ii','ipi','pis','cofins','icms')
    list_display_links = ('codigo',)
    list_per_page = 10
    search_fields = ('codigo',)


admin.site.register(Produto,ProdutoAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Departamento,DepartamentoAdmin)
admin.site.register(Tipo,TipoAdmin)
admin.site.register(Divisao,DivisaoAdmin)
admin.site.register(Marca,MarcaAdmin)
admin.site.register(Ncm,NcmAdmin)
