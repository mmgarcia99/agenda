from django.db import models
from home.models import Pessoa

class Cliente(Pessoa):
    endereco = models.CharField('Endereço', max_length=100, help_text='Endereço completo')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return super().nome
