from datetime import date

from django.utils import timezone

from .models import Especialidade, Paciente, Medico, Consulta


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

class MedicoService:
    @staticmethod
    def validar(crm, telefone):
        if not crm:
            raise ValueError("O campo CRM é obrigatório e não pode estar vazio.")

        if len(telefone) < 8:
            raise ValueError("O telefone deve possuir pelo menos 8 dígitos")

    @staticmethod
    def criar(nome, crm, telefone, especialidade):
        MedicoService.validar(crm, telefone)

        return Medico.objects.create(
            nome=nome,
            crm=crm,
            telefone=telefone,
            especialidade=especialidade
        )

class ConsultaService:
    @staticmethod
    def validar(data_hora):
        if data_hora <= timezone.now():
            raise ValueError("A consulta deve ser marcada para uma data futura.")

    @staticmethod
    def criar(medico, paciente, data_hora, observacoes, status):
        ConsultaService.validar(data_hora)

        return Consulta.objects.create(
            medico=medico,
            paciente=paciente,
            data_hora=data_hora,
            observacoes=observacoes,
            status=status
        )
