from rest_framework import serializers

from .models import Paciente, Proprietario, AnamneseGeral, AnamneseEspecial, ExameObjetivo, ExameComplementar, Medicacao, Conclusao, Observacao

class PacienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Paciente
        fields = '__all__'
class ProprietarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proprietario
        fields = '__all__'
class AnamneseGeralSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnamneseGeral
        fields = '__all__'
class AnamneseEspecialSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnamneseEspecial
        fields = '__all__'
class ExameObjetivoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExameObjetivo
        fields = '__all__'
class ExameComplementarSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExameComplementar
        fields = '__all__'
class MedicacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medicacao
        fields = '__all__'
class ConclusaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Conclusao
        fields = '__all__'
class ObservacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Observacao
        fields = '__all__'