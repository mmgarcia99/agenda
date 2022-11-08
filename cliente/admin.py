from django.contrib import admin
from cliente.models import Cliente
from django.utils.html import format_html
# Register your models here.


@admin.register(Cliente)
class ClienteAdmin (admin.ModelAdmin):
    fields = ('nome', 'endereco', 'fone', 'email', 'foto', 'fotografia')
    list_display = ('nome', 'fone', 'email')
    readonly_fields = ['fotografia']

    def fotografia(self, obj):
        if obj.foto:
            return format_html('<img width="75px" src="{}"/>', obj.foto.url)
        pass