
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, ProjetoViewSet, AtividadeViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'projetos', ProjetoViewSet)
router.register(r'atividades', AtividadeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
