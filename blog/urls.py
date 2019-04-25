from django.urls import path
from . import views

urlpatterns = [
    path('post_list/', views.post_list, name='post_list'),
    path('index', views.login, name='index'),
    path('servicos/', views.servicos, name='servicos'),
    path('cadastrar_pessoa/', views.cadastrar_pessoa, name='cadastrar_pessoa'),
    path('cadastrar_evento/', views.cadastrar_evento, name='cadastrar_evento'),
    path('cadastrar_usuario/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('caixa_geral/', views.caixa_geral, name='caixa_geral'),
    path('consultas/', views.consultas, name='consultas'),
    path('doacoes/', views.doacoes, name='doacoes'),
    path('', views.loginRegistration, name='login'),
]
