from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from data.models import Pesquisa, Respostas
from .form import PesquisaForm

@login_required(login_url="/auth/login")
def pesquisas(request):
    pesquisas = [
        {"titulo": pesquisa.titulo, "id": pesquisa.id, "feito": True}
        if not Respostas.objects.filter(usuario=request.user, pesquisa=pesquisa).exists()
        else {"titulo": pesquisa.titulo, "id": pesquisa.id, "feito": False}
        for pesquisa in Pesquisa.objects.all()
    ]
            
    print(pesquisas)
    
    return render(request, "searchs.html", {"pesquisas": pesquisas})

@login_required(login_url="/auth/login")
def pesquisa(request, pesquisa_id):
    if request.method == "GET":
        pesquisa = Pesquisa.objects.get(id=pesquisa_id)
        form = PesquisaForm(pesquisa=pesquisa.perguntas)
        return render(request, "search.html", {"form": form, "pesquisa_id": pesquisa_id, "titulo": pesquisa.titulo})
    if request.method == "POST":
        data = request.POST.copy()
        data.pop('csrfmiddlewaretoken', None)
        
        pesquisa_obj = Pesquisa.objects.get(id=pesquisa_id)
        respostas = Respostas(usuario=request.user, pesquisa=pesquisa_obj, respostas=data)
        respostas.save()
        return redirect("homepage")