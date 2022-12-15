# Generated by Django 4.1.4 on 2022-12-15 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=256, verbose_name='Nome do Paciente')),
                ('especie', models.CharField(choices=[('CANINO', 'CANINO'), ('FELINO', 'FELINO'), ('OUTROS', 'OUTROS')], max_length=16, verbose_name='Espécie do Paciente')),
                ('raca', models.CharField(choices=[('Abissínio', 'Abissínio'), ('Angorá', 'Angorá'), ('Ashera', 'Ashera'), ('Balinês', 'Balinês'), ('Bengal', 'Bengal'), ('Bobtail americano', 'Bobtail americano'), ('Bobtail japonês', 'Bobtail japonês'), ('Bombay', 'Bombay'), ('Burmês', 'Burmês'), ('Chartreux', 'Chartreux'), ('Colorpoint de Pêlo Curto', 'Colorpoint de Pêlo Curto'), ('Cornish Rex', 'Cornish Rex'), ('Curl Americano', 'Curl Americano'), ('Devon Rex', 'Devon Rex'), ('Himalaio', 'Himalaio'), ('Jaguatirica', 'Jaguatirica'), ('Javanês', 'Javanês'), ('Korat', 'Korat'), ('LaPerm', 'LaPerm'), ('Maine Coon', 'Maine Coon'), ('Manx', 'Manx'), ('Cymric', 'Cymric'), ('Mau Egípcio', 'Mau Egípcio'), ('Mist Australiano', 'Mist Australiano'), ('Munchkin', 'Munchkin'), ('Norueguês da Floresta', 'Norueguês da Floresta'), ('Pelo curto americano', 'Pelo curto americano'), ('Pelo curto brasileiro', 'Pelo curto brasileiro'), ('Pelo curto europeu', 'Pelo curto europeu'), ('Pelo curto inglês', 'Pelo curto inglês'), ('Pelo curto Oriental', 'Pelo curto Oriental'), ('Persa', 'Persa'), ('Pixie-bob', 'Pixie-bob'), ('Ragdoll', 'Ragdoll'), ('Ocicat', 'Ocicat'), ('Russo Azul', 'Russo Azul'), ('Sagrado da Birmânia', 'Sagrado da Birmânia'), ('Savannah', 'Savannah'), ('Scottish Fold', 'Scottish Fold'), ('Selkirk Rex', 'Selkirk Rex'), ('Siamês', 'Siamês'), ('Siberiano', 'Siberiano'), ('Singapura', 'Singapura'), ('Somali', 'Somali'), ('Sphynx', 'Sphynx'), ('Thai', 'Thai'), ('Tonquinês', 'Tonquinês'), ('Toyger', 'Toyger'), ('Usuri', 'Usuri'), ('Sem raça definida (SRD)', 'Sem raça definida (SRD)')], max_length=32, verbose_name='Raça do Paciente')),
                ('idade', models.CharField(max_length=3, verbose_name='Idade do Paciente')),
                ('corPelagem', models.CharField(choices=[('Azul', 'Azul'), ('Bege', 'Bege'), ('Branco', 'Branco'), ('Canela e Chocolate', 'Canela e Chocolate'), ('Chocolate', 'Chocolate'), ('Cinza', 'Cinza'), ('Creme', 'Creme'), ('Lilás', 'Lilás'), ('Marrom-escuro', 'Marrom-escuro'), ('Negro', 'Negro'), ('Vermelho', 'Vermelho')], max_length=64, verbose_name='Cor do pelo do Paciente')),
                ('dataEntrada', models.DateTimeField(auto_now_add=True, verbose_name='Data de Entrada do Paciente')),
            ],
        ),
    ]
