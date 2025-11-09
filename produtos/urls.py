'''
    Aqui dentro serão criadas as urls ( as rotas ) que vão chamar as views do arquivo
    views.py do app produtos.
'''
from django.urls import path
from . import views # . significa uma importação DESTE diretório ( produtos )

urlpatterns = [
    path('ver_produto/', views.ver_produto, name='ver_produto'),
    path('inserir_produto/', views.inserir_produto, name='inserir_produto'),
]