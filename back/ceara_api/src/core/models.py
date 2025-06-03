"""Models"""

from django.db import models


class ItemMuseu(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data = models.DateField(auto_now_add=True)


class Quiz(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Pergunta(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="perguntas")
    texto = models.CharField(max_length=255)

    def __str__(self):
        return self.texto


class Alternativa(models.Model):
    pergunta = models.ForeignKey(
        Pergunta, on_delete=models.CASCADE, related_name="alternativas"
    )
    texto = models.CharField(max_length=255)
    correta = models.BooleanField(default=False)
