from django.db import models

class Especialidade(models.Model):
    nome = models.CharField(
        max_length=100,
        unique=True
    )
    descricao = models.CharField(max_length=500)

    def __str__(self):
        return self.nome


class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(
        max_length=11,
        unique=True
    )
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Medico(models.Model):
    nome = models.CharField(max_length=100)
    crm = models.CharField(max_length=20, unique=True)
    telefone = models.CharField(max_length=20)
    especialidade = models.ForeignKey(
        'Especialidade',
        on_delete=models.CASCADE,
        related_name='medicos'
    )

    def __str__(self):
        return f'{self.nome} - {self.crm}'