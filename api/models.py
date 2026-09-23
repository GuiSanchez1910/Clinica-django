from django.db import models

class Especialidade(models.Model):
    nome = models.CharField(
        max_length=100,
        unique=True
    )
    descricao = models.CharField(max_length=500)

    def __str__(self):
        return self.nome