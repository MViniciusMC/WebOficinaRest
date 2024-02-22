from django.contrib import admin
from .models import Veiculos


@admin.register(Veiculos)
class VeiculosAdmin(admin.ModelAdmin):
    list_display = ('placa', 'ano', 'modelo')

