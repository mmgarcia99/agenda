from django import forms

from .models import Funcionario


class FuncionarioModelForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'funcao', 'fone', 'email', 'data_admissao', 'foto']
        widgets ={
            'nome': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o nome do Funcionario'}),
            'funcao': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite a função do Funcionario'}),
            'fone': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o numero do telefone'}),
            'email': forms.EmailInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o e-mail do Funcionario'}),
            'data_admissao': forms.DateInput(
                attrs={'class': 'input', 'placeholder': 'Digite a data de Admissão do Funcionario'}),
            'foto': forms.FileInput(attrs={'class': 'input', 'type': 'file'}),
        }