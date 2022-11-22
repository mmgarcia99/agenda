from django.contrib import admin
from .models import Servico
# Register your models here.

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao', 'preco']