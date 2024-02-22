from unittest.util import _MAX_LENGTH
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Veiculos(models.Model):
    
    chassi = models.CharField(max_length=16, unique=True)
    modelo = models.CharField(max_length=20)
    ano = models.CharField(max_length=4)
    placa = models.CharField(max_length=7, unique=True)
    def get_absolute_url(self):
        return reverse('veiculo Detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.modelo}, {self.placa}'
    class Meta:

        db_table = 'veiculos'
    
    
    
    