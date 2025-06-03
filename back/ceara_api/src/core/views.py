"""Views"""

from django.shortcuts import render
from rest_framework import viewsets

from .models import Alternativa, ItemMuseu, Pergunta, Quiz
from .serializers import (
    AlternativaSerializer,
    ItemMuseuSerializer,
    PerguntaSerializer,
    QuizSerializer,
)


class ItemMuseuViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ItemMuseu.objects.all()
    serializer_class = ItemMuseuSerializer


class QuizViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class PerguntaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Pergunta.objects.all()
    serializer_class = PerguntaSerializer


class AlternativaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Alternativa.objects.all()
    serializer_class = AlternativaSerializer
