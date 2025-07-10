"""Views"""

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView

from .models import Alternativa, Museu, Pergunta, Quiz, Historico
from .serializers import (
    AlternativaSerializer,
    MuseuSerializer,
    PerguntaSerializer,
    QuizSerializer,
    HistoricoSerializer,
)


class MuseuViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Museu.objects.all()
    serializer_class = MuseuSerializer


class QuizViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuizCompletoView(RetrieveAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class PerguntaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Pergunta.objects.all()
    serializer_class = PerguntaSerializer


class AlternativaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Alternativa.objects.all()
    serializer_class = AlternativaSerializer


class HistoricoViewSet(viewsets.ModelViewSet):
    serializer_class = HistoricoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Historico.objects.filter(user=self.request.user).order_by('-data')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PerfilView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        historico = Historico.objects.filter(user=user).order_by('-data')
        historico_serializado = HistoricoSerializer(historico, many=True).data

        perfil_data = {
            "nome": user.get_full_name() or user.username,
            "data_entrada": user.date_joined,
            "foto": None,
            "historico": historico_serializado
        }

        return Response(perfil_data)
