from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from data.models import Pesquisa

@login_required(login_url="/auth/login")
def pesquisas(request):
    pesquisas = Pesquisa.objects.all()
    print(pesquisas)
    
    return render(request, "searchs.html", {"pesquisas": pesquisas})

@login_required(login_url="/auth/login")
def pesquisa(request, pesquisa_id):
    pesquisa = Pesquisa.objects.get(id=pesquisa_id)
    return render(request, "search.html", {"pesquisa": pesquisa.perguntas})