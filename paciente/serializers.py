from rest_framework import serializers

from .models import Paciente, Proprietario

class PacienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Paciente
        fields = '__all__'
class ProprietarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proprietario
        fields = '__all__'