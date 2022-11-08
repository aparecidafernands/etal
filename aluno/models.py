from django.db import models

# Create your models here.
LISTA_CURSO = [
    ('Apicultura','Apicultura'), 
    ('Alimentos', 'Alimentos'),
    ('Informática','Informática'),
]

class Aluno (models.Model):
    nome = models.CharField (max_length =150)
    cpf = models.CharField (max_length =150)
    nascimento = models.DateField()
    email = models.EmailField()
    endereco = models.CharField(max_length=150)
    curso = models.CharField (max_length =150, choices = LISTA_CURSO)

    def __str__(self) -> str:
        return self.nome
