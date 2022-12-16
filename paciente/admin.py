from django.contrib import admin
from .models import Paciente, Proprietario, AnamneseGeral, AnamneseEspecial, ExameObjetivo, ExameComplementar, Medicacao, Conclusao, Observacao

# Register your models here.


class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'especie', 'raca', 'idade',
                    'corPelagem', 'dataEntrada')


admin.site.register(Paciente, PacienteAdmin)


class ProprietarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'celularTelefone', 'endereco')


admin.site.register(Proprietario, ProprietarioAdmin)


class AnamneseGeralAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'queixaPrincipal', 'historicoDoencaAtual',
                    'antecedentesMorbidos', 'CondicaoDeVida',)


admin.site.register(AnamneseGeral, AnamneseGeralAdmin)


class AnamneseEspecialAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'olhos', 'ouvidos',
                    'sr', 'sc', 'sd', 'sgu', 'sn', 'historicoImunizacao')


admin.site.register(AnamneseEspecial, AnamneseEspecialAdmin)


class ExameObjetivoAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'temperaturaRetal', 'ectoscopia',
                    'srNariz', 'srTorazInspecaoFr', 'tipoMovimento',
                    'polpacao', 'percussao', 'aucusticaPulmonar', 'scCoracaoFc',
                    'ritmo', 'aucusticaPalpacao', 'pulsoArterial',
                    'alteracoesVasculares', 'shlLifonodos', 'baco',
                    'sdViasDigestoriasAnteriores', 'abdomen', 'estomago',
                    'intestinos', 'figado', 'sgu', 'sn',
                    'orgaosSentidosOlhosOuvidos', 'aparelhoLocomotor',
                    'apreciacaoAchados', 'diagProvisorio')


admin.site.register(ExameObjetivo, ExameObjetivoAdmin)


class ExamesComplementaresAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'examesComplementares', 'anexo')


admin.site.register(ExameComplementar, ExamesComplementaresAdmin)

class MedicacaoAdmin(admin.ModelAdmin):
    list_display = ('nomeRemedio', 'dose', 'frequencia', 'duracao')


admin.site.register(Medicacao, MedicacaoAdmin)

class ConclusaoAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'diagPrincipal', 'outrosDiags', 'prognostico', 'tratamentoPrescrito', 'medicacao', 'obs')


admin.site.register(Conclusao, ConclusaoAdmin)

class ObservacoesAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'observacoesAdd')


admin.site.register(Observacao, ObservacoesAdmin)