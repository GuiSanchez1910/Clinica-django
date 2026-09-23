from rest_framework import serializers, viewsets
from .models import Especialidade
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import EspecialidadeSerializer
from .services import EspecialidadeService
from .filters import EspecialidadeFilter

class EspecialidadeViewSet(viewsets.ModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = EspecialidadeFilter

    def perform_create(self, serializer):
        try:
            EspecialidadeService.criar(
                nome=serializer.validated_data["nome"],
                descricao=serializer.validated_data["descricao"]
            )
        except ValueError as e:
            raise serializers.ValidationError(str(e))