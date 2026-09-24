from rest_framework import serializers
from .models import Especialidade, Paciente, Medico

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

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = [
            "id",
            "nome",
            "crm",
            "telefone",
            "especialidade",
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if instance and hasattr(instance, 'especialidade') and instance.especialidade:
            representation['especialidade'] = instance.especialidade.nome

        return representation