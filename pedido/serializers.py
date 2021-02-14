from .models import Pedido,Item,Cliente
from rest_framework import serializers


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['codigoProduto', 'nome', 'ean','preco','quantidade']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nomeFantasia', 'razaoSocial', 'cpfCnpj','endereco','numero','complemento','bairro','cidade','estado','cep']


class PedidoSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    cliente = ClienteSerializer(many=False)

    class Meta:
        model = Pedido
        fields = [
              'cliente',
              'status',
              'total',
              'dataCriacao',
              'dataAtualizacao',
              'nfe',
              'items'

        ]
