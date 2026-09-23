from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EspecialidadeViewSet


router = DefaultRouter()

router.register(
    r"especialidades",
    EspecialidadeViewSet,
    basename="especialidade"
)

urlpatterns = router.urls