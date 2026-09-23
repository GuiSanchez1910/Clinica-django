from .models import Especialidade


class EspecialidadeService:

    @staticmethod
    def criar(nome, descricao):
        if len(descricao.strip()) <= 5:
            raise ValueError(
                "A descrição deve ter mais de 5 caracteres."
            )

        return Especialidade.objects.create(
            nome=nome,
            descricao=descricao
        )