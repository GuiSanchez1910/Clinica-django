from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EspecialidadeViewSet, PacienteViewSet


router = DefaultRouter()

router.register(
    r"especialidades",
    EspecialidadeViewSet,
    basename="especialidade"
)

router.register(
    r"pacientes",
    PacienteViewSet,
    basename="paciente"
)

urlpatterns = router.urls