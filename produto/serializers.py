from .models import Produto
from rest_framework import serializers

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = [
              'codigo',
              'codigoFornecedor',
              'ean',
              'nome',
              'descricao',
              'categoria',
              'divisao',
              'tipo',
              'departamento',
              'marca',
              'foto',
              'origem',
              'ncm',
              'classificacao',
              'sped',
              'fornecedor',
              'dataCadatro',
              'fci',
              'impostos',
              'despesasImportacao',
              'valorFob',
              'despesasOperacionais',
              'dataCompra',
            ]

