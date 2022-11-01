from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=50, help_text='Nome do Produto')
    preco = models.DecimalField('Preço', max_digits=6, decimal_places=2, help_text='Preço do produto')
    fornecedor = models.CharField('Fornecedor', max_length=50, help_text='Nome do Fornecedor')
    quantidade = models.DecimalField('Quantidade', max_digits=5, decimal_places=2, help_text='Quantidade em estoque do produto')

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produto'

    def __str__(self):
        return self.nome