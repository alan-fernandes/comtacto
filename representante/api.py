from rest_framework import status

from representante.models import Representante
from representante.serializers import RepresentanteSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET','POST'])
def representante_list(request):
    if request.method == 'GET':
        representante = Representante.objects.all()
        serializer = RepresentanteSerializer(representante, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RepresentanteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def representante_detail_change_and_delete(request,pk):
    try:
        representante = Representante.objects.get(pk=pk)
    except Representante.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RepresentanteSerializer(representante)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = RepresentanteSerializer(representante, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        representante.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
