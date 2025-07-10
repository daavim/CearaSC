"""Serializers"""

from rest_framework import serializers

from .models import Alternativa, Museu, Pergunta, Quiz, Historico, Jogador, Perfil


class MuseuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Museu
        fields = "__all__"

class AlternativaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alternativa
        fields = ['id', 'texto', 'correta']


class PerguntaSerializer(serializers.HyperlinkedModelSerializer):
    alternativas = AlternativaSerializer(many=True, read_only=True)

    class Meta:
        model = Pergunta
        fields = ['id', 'texto', 'alternativas']


class QuizSerializer(serializers.HyperlinkedModelSerializer):
    perguntas = PerguntaSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ['id', 'titulo', 'descricao', 'perguntas']




class HistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historico
        fields = "__all__"
        read_only_fields = ['user']


class JogadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogador
        fields = ['id', 'nome', 'sobrenome', 'idade', 'posicao']


class FotoPerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = ['foto']
