import django_filters

from .models import Especialidade, Paciente, Medico


class EspecialidadeFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(
        field_name="nome",
        lookup_expr="icontains"
    )

    class Meta:
        model = Especialidade
        fields = ["nome"]


class PacienteFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(
        field_name="nome",
        lookup_expr="icontains"
    )

    class Meta:
        model = Paciente
        fields = ["nome"]

class MedicoFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(
        field_name="nome",
        lookup_expr="icontains"
    )

    crm = django_filters.CharFilter(
        field_name="crm",
        lookup_expr="icontains"
    )

    especialidade = django_filters.CharFilter(
        field_name="especialidade__nome",
        lookup_expr="icontains"
    )

    class Meta:
        model = Medico
        fields = ['nome', 'crm', 'especialidade']