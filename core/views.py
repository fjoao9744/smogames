from django.shortcuts import render, redirect
from data.models import Pesquisa
import json

def homepage(request):
    return render(request, "index.html")

def create(request):
    if request.method == "GET":
        return render(request, "create.html")
    
    elif request.method == "POST":
        titulo = request.POST.get("titulo")
        perguntas = request.POST.get("json")

        pesquisa = Pesquisa(titulo=titulo, perguntas=perguntas)
        pesquisa.save()
        return redirect("homepage")

def results(request):
    ids = Pesquisa.objects.values_list('id', flat=True)
    return render(request, "results.html", {"ids": list(ids)})

