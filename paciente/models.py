from django.db import models
from rest_framework import request
ESPECIE_CHOICES = (
    ('CANINO', 'CANINO'),
    ('FELINO', 'FELINO'),
    ('OUTROS', 'OUTROS')
)
RACA_CHOICES = (
    ('RAÇAS CANINAS', (
        (u'Akita', 'Akita'),
        (u'Basset hound', 'Basset hound'),
        (u'Beagle', 'Beagle'),
        (u'Bichon frisé', 'Bichon frisé'),
        (u'Boiadeiro australiano', 'Boiadeiro australiano'),
        (u'Border collie', 'Border collie'),
        (u'Boston terrier', 'Boston terrier'),
        (u'Boxer', 'Boxer'),
        (u'Buldogue francês', 'Buldogue francês'),
        (u'Buldogue inglês', 'Buldogue inglês'),
        (u'Bull terrier', 'Bull terrier'),
        (u'Cane corso', 'Cane corso'),
        (u'Cavalier king charles spaniel', 'Cavalier king charles spaniel'),
        (u'Chihuahua', 'Chihuahua'),
        (u'Chow chow', 'Chow chow'),
        (u'Cocker spaniel inglês', 'Cocker spaniel inglês'),
        (u'Dachshund', 'Dachshund'),
        (u'Dálmata', 'Dálmata'),
        (u'Doberman', 'Doberman'),
        (u'Dogo argentino', 'Dogo argentino'),
        (u'Dogue alemão', 'Dogue alemão'),
        (u'Fila brasileiro', 'Fila brasileiro'),
        (u'Golden retriever', 'Golden retriever'),
        (u'Husky siberiano', 'Husky siberiano'),
        (u'Jack russell terrier', 'Jack russell terrier'),
        (u'Labrador retriever', 'Labrador retriever'),
        (u'Lhasa apso', 'Lhasa apso'),
        (u'Lulu da pomerânia', 'Lulu da pomerânia'),
        (u'Maltês', 'Maltês'),
        (u'Mastiff inglês', 'Mastiff inglês'),
        (u'Mastim tibetano', 'Mastim tibetano'),
        (u'Pastor alemão', 'Pastor alemão'),
        (u'Pastor australiano', 'Pastor australiano'),
        (u'Pastor de Shetland', 'Pastor de Shetland'),
        (u'Pequinês', 'Pequinês'),
        (u'Pinscher', 'Pinscher'),
        (u'Pit bull', 'Pit bull'),
        (u'Poodle', 'Poodle'),
        (u'Pug', 'Pug'),
        (u'Rottweiler', 'Rottweiler'),
        (u'Schnauzer', 'Schnauzer'),
        (u'Shar-pei', 'Shar-pei'),
        (u'Shiba', 'Shiba'),
        (u'Shih tzu', 'Shih tzu'),
        (u'Staffordshire bull terrier', 'Staffordshire bull terrier'),
        (u'Weimaraner', 'Weimaraner'),
        (u'Yorkshire', 'Yorkshire'),
        (u'--------', '--------')
    )),
    ('RAÇAS FELINAS', ((u'Abissínio', 'Abissínio'),
                       (u'Angorá', 'Angorá'),
                       (u'Ashera', 'Ashera'),
                       (u'Balinês', 'Balinês'),
                       (u'Bengal', 'Bengal'),
                       (u'Bobtail americano', 'Bobtail americano'),
                       (u'Bobtail japonês', 'Bobtail japonês'),
                       (u'Bombay', 'Bombay'),
                       (u'Burmês', 'Burmês'),
                       (u'Chartreux', 'Chartreux'),
                       (u'Colorpoint de Pêlo Curto', 'Colorpoint de Pêlo Curto'),
                       (u'Cornish Rex', 'Cornish Rex'),
                       (u'Curl Americano', 'Curl Americano'),
                       (u'Devon Rex', 'Devon Rex'),
                       (u'Himalaio', 'Himalaio'),
                       (u'Jaguatirica', 'Jaguatirica'),
                       (u'Javanês', 'Javanês'),
                       (u'Korat', 'Korat'),
                       (u'LaPerm', 'LaPerm'),
                       (u'Maine Coon', 'Maine Coon'),
                       (u'Manx', 'Manx'),
                       (u'Cymric', 'Cymric'),
                       (u'Mau Egípcio', 'Mau Egípcio'),
                       (u'Mist Australiano', 'Mist Australiano'),
                       (u'Munchkin', 'Munchkin'),
                       (u'Norueguês da Floresta', 'Norueguês da Floresta'),
                       (u'Pelo curto americano', 'Pelo curto americano'),
                       (u'Pelo curto brasileiro', 'Pelo curto brasileiro'),
                       (u'Pelo curto europeu', 'Pelo curto europeu'),
                       (u'Pelo curto inglês', 'Pelo curto inglês'),
                       (u'Pelo curto Oriental', 'Pelo curto Oriental'),
                       (u'Persa', 'Persa'),
                       (u'Pixie-bob', 'Pixie-bob'),
                       (u'Ragdoll', 'Ragdoll'),
                       (u'Ocicat', 'Ocicat'),
                       (u'Russo Azul', 'Russo Azul'),
                       (u'Sagrado da Birmânia', 'Sagrado da Birmânia'),
                       (u'Savannah', 'Savannah'),
                       (u'Scottish Fold', 'Scottish Fold'),
                       (u'Selkirk Rex', 'Selkirk Rex'),
                       (u'Siamês', 'Siamês'),
                       (u'Siberiano', 'Siberiano'),
                       (u'Singapura', 'Singapura'),
                       (u'Somali', 'Somali'),
                       (u'Sphynx', 'Sphynx'),
                       (u'Thai', 'Thai'),
                       (u'Tonquinês', 'Tonquinês'),
                       (u'Toyger', 'Toyger'),
                       (u'Usuri', 'Usuri'),
                       (u'Sem raça definida (SRD)', 'Sem raça definida (SRD)')))

)

PELAGEM_CHOICES = (
    ('CORES CANINAS', (
        (u'Marrom', 'Marrom'),
        (u'Caramelo', 'Caramelo'),
        (u'Preto', 'Preto'),
        (u'Cinza', 'Cinza'),
        (u'Bicolor', 'Bicolor'),
        (u'Tricolor', 'Tricolor'),
    )),
    ('CORES FELINAS', ((u'Azul', 'Azul'),
                       (u'Bege', 'Bege'),
                       (u'Branco', 'Branco'),
                       (u'Canela e Chocolate', 'Canela e Chocolate'),
                       (u'Chocolate', 'Chocolate'),
                       (u'Cinza', 'Cinza'),
                       (u'Creme', 'Creme'),
                       (u'Lilás', 'Lilás'),
                       (u'Marrom-escuro', 'Marrom-escuro'),
                       (u'Negro', 'Negro'),
                       (u'Vermelho', 'Vermelho')))
)
SEXO_CHOICES = (
    ('MACHO', 'MACHO'),
    ('FÊMEA', 'FÊMEA')
)


class Proprietario (models.Model):
    nome = models.CharField(
        max_length=256, verbose_name='Nome do Proprietario')
    rg = models.CharField(max_length=256, verbose_name='RG do Proprietario')
    cpf = models.CharField(max_length=14, verbose_name='CPF fo Proprietario')
    celularTelefone = models.CharField(
        max_length=15, verbose_name='Telefone para Contato')
    endereco = models.CharField(
        max_length=512, verbose_name='Local de Residencia do Proprietario')
    email = models.CharField(
        max_length=128, verbose_name='Email para Contato')

    class Meta:
        db_table = 'proprietario'

    def __str__(self):
        return self.nome


class Paciente (models.Model):
    proprietario = models.ForeignKey(
        'Proprietario', on_delete=models.PROTECT, null=True)
    nome = models.CharField(max_length=256, verbose_name='Nome do Paciente')

    especie = models.CharField(
        max_length=16, choices=ESPECIE_CHOICES, verbose_name='Espécie do Paciente', blank=False)

    raca = models.CharField(choices=RACA_CHOICES,
                            max_length=32, verbose_name='Raça do Paciente')

    idade = models.CharField(max_length=3, verbose_name='Idade do Paciente')

    sexo = models.CharField(max_length=64, choices=SEXO_CHOICES,
                            verbose_name='Sexo do Paciente', null=True)

    corPelagem = models.CharField(
        choices=PELAGEM_CHOICES, max_length=64, verbose_name='Cor do pelo do Paciente')

    dataEntrada = models.DateTimeField(
        editable=False, auto_now_add=True, blank=False, verbose_name='Data de Entrada do Paciente')

    class Meta:
        db_table = 'paciente'

    def __str__(self):
        return self.nome


class AnamneseGeral (models.Model):
    paciente = models.ForeignKey('Paciente', on_delete=models.PROTECT)

    queixaPrincipal = models.CharField(
        max_length=1024, verbose_name='Queixa Principal')

    historicoDoencaAtual = models.CharField(
        max_length=1024, verbose_name='Histórico de Doença Atual')

    antecedentesMorbidos = models.CharField(
        max_length=1024, verbose_name='Antecedentes Mórbidos')

    CondicaoDeVida = models.CharField(
        max_length=1024, verbose_name='Condição de Vida')

    def __str__(self):
        return self.queixaPrincipal


class AnamneseEspecial (models.Model):
    paciente = models.ForeignKey(
        'Paciente', on_delete=models.PROTECT, null=True)
    base = models.ForeignKey(
        'AnamneseGeral', on_delete=models.PROTECT, null=True)

    olhos = models.CharField(max_length=1024, verbose_name='Olhos')

    ouvidos = models.CharField(max_length=1024, verbose_name='Ouvidos')

    sr = models.CharField(max_length=1024, verbose_name='S.R.')

    sc = models.CharField(max_length=1024, verbose_name='S.C.')

    sd = models.CharField(max_length=1024, verbose_name='S.D.')

    sgu = models.CharField(max_length=1024, verbose_name='S.G.U.')

    sn = models.CharField(max_length=1024, verbose_name='S.N.')

    historicoImunizacao = models.CharField(
        max_length=1024, verbose_name='Histórico de imunização')


class ExameObjetivo (models.Model):
    paciente = models.ForeignKey(
        'Paciente', on_delete=models.PROTECT, null=True)
    base = models.ForeignKey(
        'AnamneseGeral', on_delete=models.PROTECT, null=True)

    temperaturaRetal = models.CharField(
        max_length=1024, verbose_name='Temperatúra Retal Cº')

    ectoscopia = models.CharField(max_length=1024, verbose_name='Ectoscopia')

    srNariz = models.CharField(max_length=1024, verbose_name='S.R. Nariz')

    srTorazInspecaoFr = models.CharField(
        max_length=1024, verbose_name='S.R. Tórax (Inspeção F.R)')

    tipoMovimento = models.CharField(
        max_length=1024, verbose_name='Tipo de movimento')

    polpacao = models.CharField(max_length=1024, verbose_name='Polpação')

    percussao = models.CharField(max_length=1024, verbose_name='Percussão')

    aucusticaPulmonar = models.CharField(
        max_length=1024, verbose_name='Aucústica Pulmonar')

    scCoracaoFc = models.CharField(
        max_length=1024, verbose_name='S.C. Coração F.C.')

    ritmo = models.CharField(max_length=1024, verbose_name='Ritmo')

    aucusticaPalpacao = models.CharField(
        max_length=1024, verbose_name='Aucústica Palpação')

    pulsoArterial = models.CharField(
        max_length=1024, verbose_name='Pulso Arterial')

    alteracoesVasculares = models.CharField(
        max_length=1024, verbose_name='Alterações Vasculares')

    shlLifonodos = models.CharField(
        max_length=1024, verbose_name='S.H.L Linfonodos')

    baco = models.CharField(max_length=1024, verbose_name='Baço')

    sdViasDigestoriasAnteriores = models.CharField(
        max_length=1024, verbose_name='S.D. Vias Digestórias Anteriores')

    abdomen = models.CharField(max_length=1024, verbose_name='Abdomen')

    estomago = models.CharField(max_length=1024, verbose_name='Estomago')

    intestinos = models.CharField(max_length=1024, verbose_name='Intestinos')

    figado = models.CharField(max_length=1024, verbose_name='Figado')

    sgu = models.CharField(max_length=1024, verbose_name='S.G.U')

    sn = models.CharField(max_length=1024, verbose_name='S.N.')

    orgaosSentidosOlhosOuvidos = models.CharField(
        max_length=1024, verbose_name='Orgão dos Sentidos, Olhos e Ouvidos')

    aparelhoLocomotor = models.CharField(
        max_length=1024, verbose_name='Aparelho Locomotor')

    apreciacaoAchados = models.CharField(
        max_length=1024, verbose_name='Apreciação dos Achados')

    diagProvisorio = models.CharField(
        max_length=1024, verbose_name='Diagnóstico Provisório')


class ExameComplementar (models.Model):
    paciente = models.ForeignKey(
        'Paciente', on_delete=models.PROTECT, null=True)
    base = models.ForeignKey(
        'AnamneseGeral', on_delete=models.PROTECT, null=True)

    examesComplementares = models.CharField(
        max_length=1024, verbose_name='Exames Complementares')

    anexo = models.FileField(upload_to='base')

    def __str__(self):
        return self.examesComplementares


class Medicacao(models.Model):
    nomeRemedio = models.CharField(
        max_length=256, verbose_name='Nome do medicamento')

    dose = models.CharField(max_length=4, verbose_name='Dose(Mg/Kg)')

    frequencia = models.CharField(max_length=64, verbose_name='Frequencia')

    duracao = models.CharField(max_length=10, verbose_name='Duração')

    def __str__(self):
        return self.nomeRemedio


class Conclusao (models.Model):
    base = models.ForeignKey(
        'AnamneseGeral', on_delete=models.PROTECT, null=True)
    paciente = models.ForeignKey(
        'Paciente', on_delete=models.PROTECT, null=True)

    diagPrincipal = models.CharField(
        max_length=1024, verbose_name='Diagnóstico Principal')

    outrosDiags = models.CharField(
        max_length=1024, verbose_name='Outros Diagnósticos')

    prognostico = models.CharField(max_length=1024, verbose_name='Prognóstico')

    tratamentoPrescrito = models.CharField(
        max_length=1024, verbose_name='Tratamento Prescrito')

    medicacao = models.ForeignKey(Medicacao, on_delete=models.CASCADE, null=True, blank=True)


    obs = models.CharField(max_length=1024, verbose_name='OBS')

    def __str__(self):
        return self.diagPrincipal

class Observacao (models.Model):
    base = models.ForeignKey(
        'AnamneseGeral', on_delete=models.PROTECT, null=True)
    paciente = models.ForeignKey(
        'Paciente', on_delete=models.PROTECT, null=True)

    observacoesAdd = models.CharField(
        max_length=2048, verbose_name='Observações Adicionais')

    def __str__(self):
        return self.observacoesAdd
