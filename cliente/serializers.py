from .models import Cliente
from rest_framework import serializers

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
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
              'representante',
              'endereco',
              'numero',
              'complemento',
              'bairro',
              'cidade',
              'estado',
              'cep',
              'enderecoEntrega',
              'numeroEntrega',
              'complementoEntrega',
              'bairroEntrega',
              'cidadeEntrega',
              'estadoEntrega',
              'cepEntrega',
        ]