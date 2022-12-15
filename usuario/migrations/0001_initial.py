# Generated by Django 4.1.4 on 2022-12-15 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=256, verbose_name='Nome do Usuário')),
                ('cpf', models.CharField(max_length=14, verbose_name='CPF do Usuário')),
                ('senha', models.CharField(max_length=64, verbose_name='Senha de acesso do Usuário')),
                ('email', models.CharField(max_length=256, verbose_name='Email do Usuário')),
                ('cargo', models.CharField(choices=[('PROFESSOR', (('PROFESSOR', 'PROFESSOR'), ('DIRETOR', 'DIRETOR'), ('MEDICO', 'MEDICO'), ('ENFERMEIRO', 'ENFERMEIRO'))), ('ALUNO', (('ALUNO', 'ALUNO'), ('ADMINISTRATIVO', 'ADMINISTRATIVO'), ('ENFERMEIRO', 'EMFERMEIRO'), ('ESTAGIARIO', 'ESTAGIARIO'), ('RESIDENTE', 'RESIDENTE')))], max_length=32, verbose_name='Cargo do Usuário')),
            ],
        ),
    ]
