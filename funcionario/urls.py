from django.urls import path
from .views import FuncionarioView

urlpatterns = [
    path('funcionarios', FuncionarioView.as_view(), name='funcionarios'),
]