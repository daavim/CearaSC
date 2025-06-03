"""Urls (core)"""

from django.urls import include, path
from rest_framework import routers

from .views import AlternativaViewSet, ItemMuseuViewSet, PerguntaViewSet, QuizViewSet

router = routers.DefaultRouter()
router.register(r"museu", ItemMuseuViewSet)
router.register(r"quiz", QuizViewSet)
router.register(r"perguntas", PerguntaViewSet)
router.register(r"alternativas", AlternativaViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
