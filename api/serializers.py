from rest_framework import serializers
from .models import Especialidade, Paciente

class EspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidade
        fields = [
            "id",
            "nome",
            "descricao",
        ]


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = [
            "id",
            "nome",
            "cpf",
            "data_nascimento",
            "telefone",
        ]