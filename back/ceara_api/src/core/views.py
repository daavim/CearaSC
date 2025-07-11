"""Views"""

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status

from .models import Alternativa, Museu, Pergunta, Quiz, Historico, Jogador, Perfil
from .serializers import (
    AlternativaSerializer,
    MuseuSerializer,
    PerguntaSerializer,
    QuizSerializer,
    HistoricoSerializer,
    JogadorSerializer, 
    FotoPerfilSerializer
)


class MuseuViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Museu.objects.all().order_by('ano')
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


class JogadorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Jogador.objects.all()
    serializer_class = JogadorSerializer


class HistoricoViewSet(viewsets.ModelViewSet):
    queryset = Historico.objects.all()
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

        perfil = getattr(user, 'perfil', None)
        foto_url = request.build_absolute_uri(perfil.foto.url) if perfil and perfil.foto else None


        perfil_data = {
            "nome": user.get_full_name() or user.username,
            "data_entrada": user.date_joined,
            "foto": foto_url,
            "historico": historico_serializado
        }

        return Response(perfil_data)


class AtualizarFotoPerfilView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def patch(self, request):
        perfil = request.user.perfil  # Garante que já exista o perfil com OneToOne
        serializer = FotoPerfilSerializer(perfil, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'novaUrlDaFoto': serializer.data['foto']
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
