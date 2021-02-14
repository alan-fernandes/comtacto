from django.db import models
from produto.models import Produto


class Endereco(models.Model):
    nome = models.CharField(max_length=100)

class Armazenamento(models.Model):
    enderecos = models.ManyToManyField(Endereco,)
    produtos = models.ManyToManyField(Produto)

class Estoque(models.Model):
    estoque = models.IntegerField()  # produtos disponiveis pra venda
    estoqueTerceiros = models.IntegerField()  # produtos reservados ou em terceiros
    estoqueProducao = models.IntegerField()  # produtos em SKD ou recem chegados
    estoqueAvariados = models.IntegerField()  # produtos com defeitos porém com possibilidade de venda
    dataInventario = models.DateTimeField()
    prod = models.ForeignKey(Produto, on_delete=models.CASCADE,default='')
