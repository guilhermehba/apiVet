from django.db import models

FUNCTION_CHOICES = (
    ('PROFESSOR', (
        (u'PROFESSOR', 'PROFESSOR'),
        (u'DIRETOR', 'DIRETOR'),
        (u'MEDICO', 'MEDICO'),
        (u'ENFERMEIRO', 'ENFERMEIRO'),

    )),
    ('ALUNO', (
        (u'ALUNO', 'ALUNO'),
        (u'ADMINISTRATIVO', 'ADMINISTRATIVO'),
        (U'ENFERMEIRO', 'EMFERMEIRO'),
        (U'ESTAGIARIO', 'ESTAGIARIO'),
        (U'RESIDENTE', 'RESIDENTE'),
    ))
)

# Create your models here.


class Usuario (models.Model):
    nome = models.CharField(max_length=256, verbose_name='Nome do Usuário')

    cpf = models.CharField(max_length=14, verbose_name='CPF do Usuário')
    
    senha = models.CharField(
        max_length=64, verbose_name='Senha de acesso do Usuário')
    
    email = models.CharField(max_length=256, verbose_name='Email do Usuário')
    
    cargo = models.CharField(choices=FUNCTION_CHOICES,
                             max_length=32, verbose_name='Cargo do Usuário')

    class Meta:
        db_table = 'usuario'
    def __str__(self):
        return self.nome