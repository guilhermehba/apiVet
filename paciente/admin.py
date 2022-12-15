from django.contrib import admin
from .models import Paciente, Proprietario

# Register your models here.


class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'especie', 'raca', 'idade',
                    'corPelagem', 'dataEntrada')


admin.site.register(Paciente, PacienteAdmin)
class ProprietarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'celularTelefone', 'endereco')


admin.site.register(Proprietario, ProprietarioAdmin)

