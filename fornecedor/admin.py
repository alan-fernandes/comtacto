from django.contrib import admin
from .models import  Fornecedor


class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('id','name','fullName','contact','phone','email')
    list_display_links = ('name','fullName')
    #list_filter = ('nome','sobrenome')
    list_per_page = 10
    search_fields = ('name','fullName','contact')


admin.site.register(Fornecedor,FornecedorAdmin)


