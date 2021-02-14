from django.db import models
from django.utils import timezone
from cidade.models import Cidades
from representante.models import Linhas,Tabelas,Representante


class Cliente(models.Model):
      UF = [
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MG', 'Minas Gerais'),
            ('MS', 'Mato Grosso do Sul'),
            ('MT', 'Mato Grosso'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PI', 'Piauí'),
            ('PE', 'Pernambuco'),
            ('PR', 'Paraná'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('RS', 'Rio Grande do Sul'),
            ('SC', 'Santa Catarina'),
            ('SE', 'Sergipe'),
            ('SP', 'São Paulo'),
            ('TO', 'Tocantins'),
      ]



      linha = models.ForeignKey(Linhas, on_delete=models.DO_NOTHING)
      nomeFantasia = models.CharField(max_length=100,blank=True)
      razaoSocial = models.CharField(max_length=100, blank=True)
      responsavel = models.CharField(max_length=100, blank=True)
      cpfCnpj = models.CharField(max_length=30, blank=True)
      InscricaoEstadual = models.CharField(max_length=30, blank=True)
      telefone = models.CharField(max_length=20, blank=True)
      celular = models.CharField(max_length=20, blank=True)
      email = models.CharField(max_length=100, blank=True)
      emailNfe = models.CharField(max_length=100, blank=True)
      emailFinanceiro = models.CharField(max_length=100, blank=True)
      dataCadatro = models.DateTimeField(default= timezone.now)
      tabela  = models.ForeignKey(Tabelas, on_delete=models.DO_NOTHING)
      representante = models.ForeignKey(Representante, on_delete=models.DO_NOTHING)

      endereco = models.CharField(max_length=100, blank=True)
      numero = models.CharField(max_length=100, blank=True)
      complemento = models.CharField(max_length=100, blank=True)
      bairro = models.CharField(max_length=100, blank=True)
      cidade = models.ForeignKey(Cidades, on_delete=models.DO_NOTHING,related_name='cidade')
      estado = models.CharField(max_length=2,default='SP', choices=UF)
      cep =  models.CharField(max_length=10, blank=True)

      enderecoEntrega = models.CharField(max_length=100, blank=True)
      numeroEntrega = models.CharField(max_length=100, blank=True)
      complementoEntrega = models.CharField(max_length=100, blank=True)
      bairroEntrega = models.CharField(max_length=100, blank=True)
      cidadeEntrega = models.ForeignKey(Cidades, on_delete=models.DO_NOTHING,related_name='Cidade_entrega')
      estadoEntrega = models.CharField(max_length=2,default='SP', choices=UF)
      cepEntrega = models.CharField(max_length=10, blank=True)

      def __str__(self):
          return self.nomeFantasia


