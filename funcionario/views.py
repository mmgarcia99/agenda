from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView
from .models import Funcionario
from home.utils import HtmlToPdf

class FuncionarioView(ListView):
    model = Funcionario
    template_name = 'funcionarios.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(FuncionarioView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(nome__icontains=buscar)


        paginator = Paginator(qs, 1)
        listagem = paginator.get_page(self.request.GET.get('page'))
        return listagem

    def get(self, *args, **kwargs):
        if self.request.GET.get('imprimir') == 'pdf':
            html_pdf = HtmlToPdf(arquivo='funcionarios_pdf', qs=self.get_queryset())
            return html_pdf.response
        else:
            return super(FuncionarioView, self).get(*args, **kwargs)