from django.db import models


class Cidades(models.Model):
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

    nome = models.CharField(max_length=50)
    estado = models.CharField(max_length=2,default='SP',choices=UF)
    ibge = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'

    def __str__(self):
        return self.nome
