"""Admin"""

from django.contrib import admin

from .models import Alternativa, Museu, Pergunta, Quiz, Historico, Jogador, Perfil


@admin.register(Museu)
class MuseuAdmin(admin.ModelAdmin):
    list_display = ["titulo", "descricao", "ano"]


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ["titulo", "descricao", "criado_em"]


@admin.register(Pergunta)
class PerguntaAdmin(admin.ModelAdmin):
    list_display = ["quiz", "texto"]


@admin.register(Alternativa)
class AlternativaAdmin(admin.ModelAdmin):
    list_display = ["pergunta", "texto", "correta"]

@admin.register(Historico)
class HistoricoAdmin(admin.ModelAdmin):
    list_display = ["tipo", "titulo", "descricao"]

@admin.register(Jogador)
class JogadorAdmin(admin.ModelAdmin):
    list_display = ["nome", "sobrenome", "idade", "posicao"]

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ["foto"]
