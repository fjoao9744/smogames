from django.http import JsonResponse
from data.models import Pessoa

def data(request):
    dados = list(Pessoa.objects.values('id', 'user_id', 'perguntas'))  # ou os campos que quiser
    print(dados)
    return JsonResponse(dados, safe=False)
