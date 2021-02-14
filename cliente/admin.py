from django.contrib import admin
from .models import  Cliente
from representante.models import Linhas,Tabelas
from cidade.models import Cidades

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id','responsavel','nomeFantasia','razaoSocial','telefone','email')
    list_display_links = ('responsavel','nomeFantasia')
    #list_filter = ('nome','sobrenome')
    list_per_page = 10
    search_fields = ('responsavel','nomeFantasia','razaoSocial')



class TabelaAdmin(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links = ('nome',)
    list_per_page = 10
    search_fields = ('nome',)

class LinhaAdmin(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links = ('nome',)
    list_per_page = 10
    search_fields = ('nome',)

class CidadeAdmin(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links = ('nome',)
    list_per_page = 10
    search_fields = ('nome',)


admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Cidades,CidadeAdmin)
admin.site.register(Tabelas,TabelaAdmin)
admin.site.register(Linhas,LinhaAdmin)
