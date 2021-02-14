from django.db import models
from django.utils import timezone


class Fornecedor(models.Model):

      name = models.CharField(max_length=100,blank=True)
      fullName = models.CharField(max_length=100, blank=True)
      contact = models.CharField(max_length=100, blank=True)
      phone = models.CharField(max_length=20, blank=True)
      mobile = models.CharField(max_length=20, blank=True)
      email = models.CharField(max_length=100, blank=True)
      date = models.DateTimeField(default= timezone.now)
      address = models.CharField(max_length=100, blank=True)
      address_c = models.CharField(max_length=100, blank=True)
      city = models.CharField(max_length=100, blank=True)
      country = models.CharField(max_length=100, blank=True)
      state = models.CharField(max_length=100, blank=True)
      zip =  models.CharField(max_length=15, blank=True)
      #Informaçoes de importação
      taxRefund = models.CharField(max_length=1, blank=True)
      incoterm = models.CharField(max_length=40, blank=True)
      paymentTerm = models.CharField(max_length=200, blank=True)
      #dados de pagamento ao fornecedor
      bankName = models.CharField(max_length=200, blank=True)
      bankAddress = models.CharField(max_length=200, blank=True)
      bankAccount = models.CharField(max_length=50, blank=True)
      bankIban = models.CharField(max_length=50, blank=True)
      bankSwift = models.CharField(max_length=50, blank=True)



      def __str__(self):
          return self.name


