from rest_framework import status

from pedido.models import Pedido
from pedido.serializers import PedidoSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET','POST'])
def pedido_list(request):
    if request.method == 'GET':
        pedido = Pedido.objects.all()
        serializer = PedidoSerializer(pedido, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PedidoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def pedido_detail_change_and_delete(request,pk):
    try:
        pedido = Pedido.objects.get(pk=pk)
    except Pedido.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PedidoSerializer(pedido)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PedidoSerializer(pedido, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        pedido.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
