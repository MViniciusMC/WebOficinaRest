from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Veiculos
from .serializers import veiculosSerializer
import re
from datetime import date


'''
class VeiculosViewSet(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        # lista de veículos
        veiculos = Veiculos.objects.all()
        
        serializer = veiculosSerializer(veiculos, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Cadastra um novo veículo
        data = {
            "chassi":request.data.get('chassi'), 
    "modelo":request.data.get('modelo'), 
    "ano":request.data.get('ano'), 
    "placa":request.data.get('placa'), 
        }
        serializer = veiculosSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# mudar o models para charfield
'''
class VeiculosViewSet(viewsets.ModelViewSet):
  queryset = Veiculos.objects.all()
  serializer_class = veiculosSerializer
  permission_classes = [IsAuthenticated]
  
  def create(self, request, *args,**kwargs):
    ano = request.data.get('ano')
    regex = re.match(r'[0-9]', ano)
    if regex == None:
        ano = "1886"
    ano_seguinte = int(date.today().year) + 1
    ano_int = int(ano)
    if ano_int < 1886 or ano_int > ano_seguinte:
        ano = "1886"
    
    # chassi não repedido nem placa por causa do models. 
    data = {"chassi":request.data.get('chassi'), 
    "modelo":request.data.get('modelo'), 
    "ano":ano, 
    "placa":request.data.get('placa'), 
        }
    serializer = veiculosSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response({"status": True,
                         "message": "Um Novo veiculo foi adicionado",
                         "data": serializer.data},
                        status=status.HTTP_201_CREATED, headers=headers)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
# acresentar lógica para não permitir a entrada de valores repitidos no banco de dados 
