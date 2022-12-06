from django.urls import path
from .views import ServicosView

urlpatterns = [
    path('servico', ServicosView.as_view(), name='servico')
]