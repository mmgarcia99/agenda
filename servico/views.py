from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic import ListView

from home.utils import HtmlToPdf
from .models import Servico


# Create your views here.
class ServicosView(ListView):
    model = Servico
    template_name = 'servicos.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(ServicosView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(Q(nome__icontains=buscar) | Q(descricao__icontains= buscar))



        paginator = Paginator(qs, 1)
        listagem = paginator.get_page(self.request.GET.get('page'))
        return listagem

    def get(self, *args, **kwargs):
        if self.request.GET.get('imprimir') == 'pdf':
            html_pdf = HtmlToPdf(arquivo='servico_pdf', qs=self.get_queryset())
            return html_pdf.response
        else:
            return super(ServicosView, self).get(*args, **kwargs)