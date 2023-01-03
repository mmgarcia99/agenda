from django.shortcuts import render
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from home.utils import HtmlToPdf
from .forms import ClienteModelForm
from .models import Cliente

class ClientesView(ListView):
    model = Cliente
    template_name = 'clientes.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(ClientesView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(nome__icontains=buscar)


        paginator = Paginator(qs, 10)
        listagem = paginator.get_page(self.request.GET.get('page'))
        return listagem

    def get(self, *args,**kwargs):
        if self.request.GET.get('imprimir') == 'pdf':
            html_pdf = HtmlToPdf(arquivo='clientes_pdf', qs=self.get_queryset())
            return html_pdf.response
        else:
            return super(ClientesView, self).get(*args, **kwargs)


class ClienteAddView(CreateView):
    form_class = ClienteModelForm
    model = Cliente
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('clientes')

class ClienteUpDateView(UpdateView):
    form_class = ClienteModelForm
    model = Cliente
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('clientes')

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'cliente_apagar.html'
    success_url = reverse_lazy('clientes')
