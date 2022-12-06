from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView
from .models import Funcionario

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
