from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from data.models import Pessoa

@login_required
def pesquisas(request):
    pessoa = Pessoa.objects.get(user=request.user)
    
    return render(request, "pesquisas.html", {"pesquisas": pessoa.pesquisas}) #type: ignore

@login_required
def pesquisa(request, pesquisa_id):
    return