from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pesquisas = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return self.user.username

class Pesquisa(models.Model):
    nome = models.TextField(default="")
    perguntas = models.JSONField(default=list)
    
    