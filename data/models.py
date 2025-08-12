from django.db import models
from django.contrib.auth.models import User

class Pesquisa(models.Model):
    titulo = models.TextField(default="")
    perguntas = models.JSONField(default=list)
    
    def __str__(self):
        return self.titulo
    
class Respostas(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pesquisa = models.ForeignKey(Pesquisa, on_delete=models.CASCADE)
    respostas = models.JSONField(default=list)
    
    data_resposta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Respostas de {self.usuario} para {self.pesquisa}"
