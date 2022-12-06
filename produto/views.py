from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView
from .models import Produto

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