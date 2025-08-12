from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from data.models import Pesquisa
from .form import PesquisaForm

@login_required(login_url="/auth/login")
def pesquisas(request):
    pesquisas = Pesquisa.objects.all()
    print(pesquisas)
    
    return render(request, "searchs.html", {"pesquisas": pesquisas})

@login_required(login_url="/auth/login")
def pesquisa(request, pesquisa_id):
    pesquisa = Pesquisa.objects.get(id=pesquisa_id)
    form = PesquisaForm(pesquisa=pesquisa.perguntas)
    return render(request, "search.html", {"form": form})