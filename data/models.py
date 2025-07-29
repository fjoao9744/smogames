from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    perguntas = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return self.user.username
