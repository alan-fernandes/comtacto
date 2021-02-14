from rest_framework import status

from fornecedor.models import Fornecedor
from fornecedor.serializers import FornecedorSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET','POST'])
def fornecedor_list(request):
    if request.method == 'GET':
        fornecedor = Fornecedor.objects.all()
        serializer = FornecedorSerializer(fornecedor, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FornecedorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def fornecedor_detail_change_and_delete(request,pk):
    try:
        fornecedor = Fornecedor.objects.get(pk=pk)
    except Fornecedor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FornecedorSerializer(fornecedor)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = FornecedorSerializer(fornecedor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        fornecedor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
