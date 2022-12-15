from .models import Paciente, Proprietario
from rest_framework import viewsets
from .serializers import PacienteSerializer, ProprietarioSerializer


class PacienteViewSet(viewsets.ModelViewSet):
    serializer_class = PacienteSerializer
    queryset = Paciente.objects.all()
class ProprietarioViewSet(viewsets.ModelViewSet):
    serializer_class = ProprietarioSerializer
    queryset = Proprietario.objects.all()
