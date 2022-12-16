from .models import Paciente, Proprietario, AnamneseGeral, AnamneseEspecial, ExameObjetivo, ExameComplementar, Medicacao, Conclusao, Observacao
from rest_framework import viewsets
from .serializers import PacienteSerializer, ProprietarioSerializer,AnamneseGeralSerializer,AnamneseEspecialSerializer, ExameObjetivoSerializer, ExameComplementarSerializer, MedicacaoSerializer,ConclusaoSerializer, ObservacaoSerializer


class PacienteViewSet(viewsets.ModelViewSet):
    serializer_class = PacienteSerializer
    queryset = Paciente.objects.all()

class ProprietarioViewSet(viewsets.ModelViewSet):
    serializer_class = ProprietarioSerializer
    queryset = Proprietario.objects.all()

class AnamneseGeralViewSet(viewsets.ModelViewSet):
    serializer_class = AnamneseGeralSerializer
    queryset = AnamneseGeral.objects.all()

class AnamneseEspecialViewSet(viewsets.ModelViewSet):
    serializer_class = AnamneseEspecialSerializer
    queryset = AnamneseEspecial.objects.all()

class ExameObjetivoViewSet(viewsets.ModelViewSet):
    serializer_class = ExameObjetivoSerializer
    queryset = ExameObjetivo.objects.all()

class ExameComplementarViewSet(viewsets.ModelViewSet):
    serializer_class = ExameComplementarSerializer
    queryset = ExameComplementar.objects.all()

class MedicacaoViewSet(viewsets.ModelViewSet):
    serializer_class = MedicacaoSerializer
    queryset = Medicacao.objects.all()

class ConclusaoViewSet(viewsets.ModelViewSet):
    serializer_class = ConclusaoSerializer
    queryset = Conclusao.objects.all()

class ObservacaoViewSet(viewsets.ModelViewSet):
    serializer_class = ObservacaoSerializer
    queryset = Observacao.objects.all()
