from django.contrib import admin
from .models import Servico
from produto.models import Produto
from produtoservico.models import ProdutoServico
# Register your models here.
class ProdutoServicoInLine(admin.TabularInline):
    model = ProdutoServico
    extra = 1

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao', 'preco', 'get_produtos',]
    inlines = [ProdutoServicoInLine]

    def get_produtos(self, obj):
        return ','.join([prd.nome for prd in Produto.objects.filter(servico=obj.id)])

    get_produtos.short_description = 'Produtos utilizados'