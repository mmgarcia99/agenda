from django.shortcuts import render

# Create your views here.
def index(request):

    context = {
        'disciplina': 'Desenvolvimento web - Tecnico em informatica - politecnico - ufsm',
        'tecnologia' : 'Python e django'
    }
    return render(request, 'index.html', context)
