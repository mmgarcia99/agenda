from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView

from home.utils import HtmlToPdf
from .models import Cliente

class ClientesView(ListView):
    model = Cliente
    template_name = 'clientes.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(ClientesView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(nome__icontains=buscar)


        paginator = Paginator(qs, 1)
        listagem = paginator.get_page(self.request.GET.get('page'))
        return listagem

    def get(self, *args,**kwargs):
        if self.request.GET.get('imprimir') == 'pdf':
            html_pdf = HtmlToPdf(arquivo='clientes_pdf', qs=self.get_queryset())
            return html_pdf.response
        else:
            return super(ClientesView, self).get(*args, **kwargs)