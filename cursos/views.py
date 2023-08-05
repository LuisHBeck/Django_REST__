from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

class CursoAPIView(APIView):
    """
    API de Cursos
    """

    def get(self, request):
        print(request.user)
        print(request.user.id)

        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)
    

class AvaliacaoAPIView(APIView):
    """
    API de Avaliações 
    """

    def get(self, request):
        print(request) 

        avalicoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avalicoes, many=True)
        return Response(serializer.data)
        