"""Models"""

from django.db import models
from django.contrib.auth.models import User


class Museu(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data = models.DateField()


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


class Historico(models.Model):
    TIPO_EVENTO_CHOICES = [
        ('quiz', 'Quiz'),
        ('palpite', 'Palpite'),
        ('outro', 'Outro'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='historicos')
    tipo = models.CharField(max_length=20, choices=TIPO_EVENTO_CHOICES)
    titulo = models.CharField(max_length=255, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.tipo} - {self.titulo}'
