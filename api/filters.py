import django_filters

from .models import Especialidade, Paciente


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