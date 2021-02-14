from django.contrib import admin
from .models import  Representante

class RepresentantesAdmin(admin.ModelAdmin):
    list_display = ('id','responsavel','nomeFantasia','razaoSocial','telefone','email')
    list_display_links = ('responsavel','nomeFantasia')
    #list_filter = ('nome','sobrenome')
    list_per_page = 10
    search_fields = ('responsavel','nomeFantasia','razaoSocial')


admin.site.register(Representante,RepresentantesAdmin)
