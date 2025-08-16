from data.models import Respostas, Pesquisa
from api.serializers import RespostaSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class RespostasAPI(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pesquisa_id=None):
        if pesquisa_id:
            pesquisa = get_object_or_404(Pesquisa, id=pesquisa_id)
            respostas = Respostas.objects.filter(pesquisa=pesquisa)
        else:
            respostas = Respostas.objects.all()
            
        serializer = RespostaSerializer(respostas, many=True)
        return Response(serializer.data)