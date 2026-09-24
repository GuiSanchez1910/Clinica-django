import django_filters

from .models import Especialidade, Paciente, Medico, Consulta


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

class ConsultaFilter(django_filters.FilterSet):
    medico = django_filters.CharFilter(
        field_name="medico__nome",
        lookup_expr="icontains"
    )

    paciente = django_filters.CharFilter(
        field_name="paciente__nome",
        lookup_expr="icontains"
    )

    status = django_filters.CharFilter(
        field_name="status",
        lookup_expr="iexact"
    )

    data_inicio = django_filters.DateFilter(
        field_name="data_hora__date",
        lookup_expr="gte"
    )

    data_fim = django_filters.DateFilter(
        field_name="data_hora__date",
        lookup_expr="lte"
    )

    class Meta:
        model = Consulta
        fields = ['medico', 'paciente', 'status', 'data_inicio', 'data_fim']
