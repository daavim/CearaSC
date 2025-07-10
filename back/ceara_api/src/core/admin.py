"""Admin"""

from django.contrib import admin

from .models import Alternativa, Museu, Pergunta, Quiz, Historico


@admin.register(Museu)
class MuseuAdmin(admin.ModelAdmin):
    list_display = ["titulo", "descricao", "data"]


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
