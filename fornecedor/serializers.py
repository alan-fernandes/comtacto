from .models import Fornecedor
from rest_framework import serializers

class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = [
              'name',
              'fullName',
              'contact',
              'phone',
              'mobile',
              'email',
              'date',
              'address',
              'address_c',
              'country',
              'city',
              'state',
              'zip',
              'taxRefund',
              'incoterm',
              'paymentTerm',
              'bankName',
              'bankAddress',
              'bankAccount',
              'bankIban',
              'bankSwift',
        ]
