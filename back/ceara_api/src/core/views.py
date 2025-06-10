"""Views"""

from django.shortcuts import render
from rest_framework import viewsets

from .models import Alternativa, Museu, Pergunta, Quiz
from .serializers import (AlternativaSerializer, MuseuSerializer,
                          PerguntaSerializer, QuizSerializer)


class MuseuViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Museu.objects.all()
    serializer_class = MuseuSerializer


class QuizViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class PerguntaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Pergunta.objects.all()
    serializer_class = PerguntaSerializer


class AlternativaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Alternativa.objects.all()
    serializer_class = AlternativaSerializer
