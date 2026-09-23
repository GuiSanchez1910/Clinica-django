from rest_framework import serializers, viewsets
from .models import Especialidade, Paciente
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import EspecialidadeSerializer, PacienteSerializer
from .services import EspecialidadeService, PacienteService
from .filters import EspecialidadeFilter, PacienteFilter

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


class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = PacienteFilter

    def perform_create(self, serializer):
        try:
            PacienteService.criar(
                nome=serializer.validated_data["nome"],
                cpf=serializer.validated_data["cpf"],
                data_nascimento=serializer.validated_data["data_nascimento"],
                telefone=serializer.validated_data["telefone"]
            )
        except ValueError as e:
            raise serializers.ValidationError(str(e))

    def perform_update(self, serializer):
        dados = serializer.validated_data
        try:
            PacienteService.validar(
                cpf=dados.get("cpf", serializer.instance.cpf),
                data_nascimento=dados.get(
                    "data_nascimento",
                    serializer.instance.data_nascimento
                )
            )
        except ValueError as e:
            raise serializers.ValidationError(str(e))

        serializer.save()