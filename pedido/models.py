from django.db import models
from cliente.models import Cliente
from django.contrib.auth.models import User


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=20, blank=True)
    total = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    dataCriacao = models.CharField(max_length=20, blank=True)
    dataAtualizacao = models.DateTimeField(max_length=20, blank=True)
    nfe = models.CharField(max_length=100, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,default=None)

    def __str__(self):
        return f'Pedido N. {self.pk}'

class Item(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE,related_name='items',default=None)
    codigoProduto = models.CharField(max_length=20)
    ean = models.CharField(max_length=20)
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    width = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    length = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    desconto = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    quantidade = models.IntegerField()
    precoBase = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name = 'Item do pedido'
        verbose_name_plural = 'Itens do pedido'





