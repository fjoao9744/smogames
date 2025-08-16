from rest_framework import serializers
from data.models import Respostas

class RespostaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Respostas
        fields = ['pesquisa', 'respostas']