from django.views.generic import TemplateView
from cliente.models import Cliente
from funcionario.models import Funcionario
from servico.models import Servico
from produto.models import Produto
from atendimento.models import Atendimento

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs ):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['qtd_clientes'] = Cliente.objects.count()
        context['qtd_funcionarios'] = Funcionario.objects.count()
        context['qtd_servicos'] = Servico.objects.count()
        context['qtd_produtos'] = Produto.objects.count()
        context['qtd_agendamentos'] = Atendimento.objects.count()
        return context