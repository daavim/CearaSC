"""Serializers"""

from rest_framework import serializers

from .models import Alternativa, Museu, Pergunta, Quiz


class MuseuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Museu
        fields = "__all__"


class QuizSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quiz
        fields = "__all__"


class PerguntaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pergunta
        fields = "__all__"


class AlternativaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alternativa
        fields = "__all__"
