from .models import Representante
from rest_framework import serializers

class RepresentanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Representante
        fields = [
              'linha',
              'nomeFantasia',
              'razaoSocial',
              'responsavel',
              'cpfCnpj',
              'InscricaoEstadual',
              'telefone',
              'celular',
              'email',
              'emailNfe',
              'emailFinanceiro',
              'dataCadatro',
              'tabela',
              'endereco',
              'numero',
              'complemento',
              'bairro',
              'cidade',
              'estado',
              'cep',
        ]
