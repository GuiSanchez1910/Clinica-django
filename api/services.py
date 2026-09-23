from datetime import date

from .models import Especialidade, Paciente


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


class PacienteService:

    @staticmethod
    def validar(cpf, data_nascimento):
        if len(cpf) != 11 or not cpf.isdigit():
            raise ValueError(
                "O CPF deve conter exatamente 11 dígitos."
            )

        if data_nascimento >= date.today():
            raise ValueError(
                "A data de nascimento deve ser anterior a hoje."
            )

    @staticmethod
    def criar(nome, cpf, data_nascimento, telefone):
        PacienteService.validar(cpf, data_nascimento)

        return Paciente.objects.create(
            nome=nome,
            cpf=cpf,
            data_nascimento=data_nascimento,
            telefone=telefone
        )