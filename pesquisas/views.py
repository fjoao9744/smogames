from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from data.models import Pessoa

@login_required(login_url="/auth/login")
def pesquisas(request):
    pessoa = Pessoa.objects.get(user=request.user)
    print(pessoa)
    
    return render(request, "pesquisas.html", {"pesquisas": pessoa.pesquisas}) #type: ignore

@login_required(login_url="/auth/login")
def pesquisa(request, pesquisa_id):
    return