from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa
# Create your views here.

def ver_produto(request):
    if request.method == 'GET':
        nome = 'Miqueias'
        return render(request, 'ver_produto.html', {'nome': nome})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        
        pessoas = Pessoa.objects.all()
        pessoa_especifica = Pessoa.objects.filter(nome=nome)
        if pessoa_especifica.exists():
            return HttpResponse('Usuário já cadastrado')
        else:
            pessoa = Pessoa(nome=nome, idade=idade)
            pessoa.save()
            return HttpResponse('Usuário cadastrado com sucesso!')


def inserir_produto(request):
    nome = 'Gustavo'
    return render(request, 'inserir_produto.html', {'nome':nome})