from django.db import models
from django.contrib.auth.models import User

class Pesquisa(models.Model):
    nome = models.TextField(default="")
    perguntas = models.JSONField(default=list)
    

def verificar_pesquisas():
    pesquisas = {str(p.id): True for p in Pesquisa.objects.all()}
    print(pesquisas)
    
    return pesquisas
    
class Pessoa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pesquisas = models.JSONField(default=verificar_pesquisas, blank=True)

    def __str__(self):
        return self.user.username

    