from django.urls import path
from . import views

urlpatterns = [
    path('servicos/', views.servicos, name='servicos'),
    path('cadastrar_pessoa/', views.cadastrar_pessoa, name='cadastrar_pessoa'),
    path('cadastrar_evento/', views.cadastrar_evento, name='cadastrar_evento'),
    path('caixa_geral/', views.caixa_geral, name='caixa_geral'),
    path('consultas/', views.consultas, name='consultas'),
    path('consultasOK/', views.consultasOK, name='consultasOK'),
    path('doacoes/', views.doacoes, name='doacoes'),
]
