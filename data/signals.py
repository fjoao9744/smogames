from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Pessoa

@receiver(post_save, sender=User)
def criar_pessoa_automaticamente(sender, instance, created, **kwargs):
    if created:
        Pessoa.objects.create(user=instance)
