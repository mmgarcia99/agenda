from django.contrib import admin
from funcionario.models import Funcionario
from django.utils.html import format_html



@admin.register(Funcionario)
class ClienteAdmin (admin.ModelAdmin):
    fields = ('nome', 'fone', 'funcao','data_admissao', 'email', 'foto', 'fotografia',)
    list_display = ('nome', 'fone', 'email', 'funcao')
    readonly_fields = ['fotografia']

    def fotografia(self, obj):
        if obj.foto:
            return format_html('<img width="75px" src="{}"/>', obj.foto.url)
        pass