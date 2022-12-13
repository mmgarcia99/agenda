from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView
from .models import Produto
from home.utils import HtmlToPdf

# Create your views here.

class ProdutoView(ListView):
    model = Produto
    template_name = 'produto.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(ProdutoView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(nome__icontains=buscar)



        paginator = Paginator(qs, 1)
        listagem = paginator.get_page(self.request.GET.get('page'))
        return listagem

    def get(self, *args, **kwargs):
        if self.request.GET.get('imprimir') == 'pdf':
            html_pdf = HtmlToPdf(arquivo='produto_pdf', qs=self.get_queryset())
            return html_pdf.response
        else:
            return super(ProdutoView, self).get(*args, **kwargs)