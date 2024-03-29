from django.db import models

# Create your models here.
class Atendimento(models.Model):
    SITUACAO_OPCOES = (
        ('A', 'Agendado'),
        ('R', 'Realizado'),
        ('C', 'Concluido')
    )
    horario = models.DateTimeField('Horário', help_text='Data e hora do atendimento')
    cliente = models.ForeignKey('cliente.Cliente', verbose_name='Cliente', help_text='Nome do cliente', on_delete=models.CASCADE)
    funcionario = models.ForeignKey('funcionario.Funcionario', verbose_name='Funcionário', help_text='Nome do Funcionario', on_delete=models.CASCADE)
    situacao = models.CharField('Situação', max_length=15, help_text='Situação do atendimento', choices=SITUACAO_OPCOES, default='A')
    servico = models.ForeignKey('servico.Servico', verbose_name='Serviço', help_text='Nome do Serviço', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Atendimento'
        verbose_name_plural = 'Atendimentos'

    def __str__(self):
        return  f'Cliente:{self.cliente} - Funcionário:{self.funcionario} - Serviço:{self.servico}'