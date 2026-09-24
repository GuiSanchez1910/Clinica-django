from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EspecialidadeViewSet, PacienteViewSet, MedicoViewSet


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

router.register(
    r'medicos',
    MedicoViewSet,
    basename="medico"
)

urlpatterns = router.urls