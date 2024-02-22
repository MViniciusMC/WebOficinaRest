from sre_compile import isstring
from django.contrib.auth.models import  User
from rest_framework import serializers
from .models import Veiculos

 

class veiculosSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Veiculos
        fields = ('chassi','modelo', 'ano', 'placa')
    
    


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')