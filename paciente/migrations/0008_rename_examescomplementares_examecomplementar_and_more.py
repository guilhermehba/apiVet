# Generated by Django 4.1.4 on 2022-12-16 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0007_delete_cpa'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ExamesComplementares',
            new_name='ExameComplementar',
        ),
        migrations.RenameModel(
            old_name='observacoes',
            new_name='Observacao',
        ),
        migrations.AddField(
            model_name='conclusao',
            name='medicacao',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='paciente.medicacao'),
        ),
    ]