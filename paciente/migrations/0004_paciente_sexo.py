# Generated by Django 4.1.4 on 2022-12-15 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0003_alter_paciente_corpelagem_alter_paciente_raca'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='sexo',
            field=models.CharField(choices=[('MACHO', 'MACHO'), ('FÊMEA', 'FÊMEA')], max_length=64, null=True, verbose_name='Sexo do Paciente'),
        ),
    ]