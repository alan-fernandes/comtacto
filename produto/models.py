from django.db import models
from django.utils import timezone
from fornecedor.models import Fornecedor

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Departamento(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Tipo(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Divisao(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Marca(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Ncm(models.Model):
    codigo = models.CharField(max_length=20)
    descricao = models.TextField()
    ii = models.CharField(max_length=10)
    ipi = models.CharField(max_length=10)
    pis = models.CharField(max_length=10)
    cofins = models.CharField(max_length=10)
    icms = models.CharField(max_length=10)


    def __str__(self):
        return self.codigo

class Produto(models.Model):
    ORIGEM_CHOICES = [
        ('0', 'Nacional, exceto as indicadas nos códigos 3, 4, 5 e 8'),
        ('1', 'Estrangeira - Importação direta, exceto a indicada no código 6'),
        ('2', 'Estrangeira - Adquirida no mercado interno, exceto a indicada no código 7'),
        ('3',
         'Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40% (quarenta por cento) e inferior ou igual a 70% (setenta por cento)'),
        ('4',
         'Nacional, cuja produção tenha sido feita em conformidade com os processos produtivos básicos de que tratam o Decreto-Lei no 288/67, e as Leis nos 8.248/91, 8.387/91, 10.176/01 e 11.484/07'),
        ('5', 'Nacional, mercadoria ou bem com Conteúdo de Importação inferior ou igual a 40% (quarenta por cento)'),
        ('6',
         'Estrangeira - Importação direta, sem similar nacional, constante em lista de Resolução CAMEX e gás natural'),
        ('7',
         'Estrangeira - Adquirida no mercado interno, sem similar nacional, constante em lista de Resolução CAMEX e gás natural'),
        ('8', 'Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70% (setenta por cento)'),
    ]
    CLASSIFICACAO_CHOICES = [
        ('0', 'Fabricação Própria'),
        ('1', 'Revenda'),
        ('2', 'Representação'),
        ('3', 'Produto Importado'),
        ('4', 'Mercadoria Consignada'),
        ('5', 'Revenda (Não Mantém Estoque)'),
        ('6', 'Fabricação Própria  (Não Mantém Estoque)'),
        ]
    STATUS = [
        ('0', 'INATIVO'),
        ('1', 'ATIVO'),
        ('2',  'NÃO COMPRAR'),
        ('3', 'DELETADO'),
    ]
    SPED_CHOICES = [
        ('00', 'Mercadoria para Revenda'),
        ('01', 'Matéria-Prima'),
        ('02', 'Embalagem'),
        ('03', 'Produto em Processo'),
        ('04', 'Produto Acabado'),
        ('05', 'Subproduto'),
        ('06', 'Produto Intermediário'),
        ('07', 'Material de Uso e Consumo'),
        ('08', 'Ativo Imobilizado'),
        ('09', 'Serviços'),
        ('10', 'Outros insumos'),
        ('99', 'Outras'),
        ]
    codigo = models.CharField(max_length=20)
    codigoFornecedor = models.CharField(max_length=50)
    ean = models.CharField(max_length=15)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    categoria = models.ForeignKey(Categoria,on_delete=models.DO_NOTHING)
    divisao = models.ForeignKey(Divisao, on_delete=models.DO_NOTHING)
    tipo = models.ForeignKey(Tipo, on_delete=models.DO_NOTHING)
    departamento = models.ForeignKey(Departamento, on_delete=models.DO_NOTHING)
    marca = models.ForeignKey(Marca, on_delete=models.DO_NOTHING)
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m/d')
    origem = models.CharField( max_length=2,choices=ORIGEM_CHOICES,default=0,)
    ncm = models.ForeignKey(Ncm, on_delete=models.DO_NOTHING)
    classificacao = models.CharField(max_length=2, choices=CLASSIFICACAO_CHOICES, default='0', )
    sped = models.CharField(max_length=2, choices=SPED_CHOICES, default='00', )
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=2, choices=STATUS, default='1', )
    dataCadatro = models.DateTimeField(default= timezone.now)

    fci  = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True) #valor formado no recebimento da mercadoria
    impostos = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True) #total de impostos na base de calculo do produto
    despesasImportacao = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True) #custos de importacao
    valorFob = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True) # valor de compra do produto
    valorDollar = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True) # valor do dollar na ultima compra
    despesasOperacionais = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)#custo da empresa

    dataCompra = models.DateTimeField() #data de chegada da última importação




