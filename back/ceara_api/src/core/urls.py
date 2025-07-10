"""Urls (core)"""

from django.urls import include, path
from rest_framework import routers

from .views import AlternativaViewSet, MuseuViewSet, PerguntaViewSet, QuizViewSet, PerfilView, QuizCompletoView

router = routers.DefaultRouter()
router.register(r"museu", MuseuViewSet)
router.register(r"quiz", QuizViewSet)
router.register(r"perguntas", PerguntaViewSet)
router.register(r"alternativas", AlternativaViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('perfil/', PerfilView.as_view(), name='perfil'),
    path('quiz/<int:pk>/completo/', QuizCompletoView.as_view(), name='quiz-completo'),
]
