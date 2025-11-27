from rest_framework import viewsets
from .models import *
from .serializers import *

class DiocesisViewSet(viewsets.ModelViewSet):
    queryset = Diocesis.objects.all()
    serializer_class = DiocesisSerializer

class ParroquiaViewSet(viewsets.ModelViewSet):
    queryset = Parroquia.objects.all()
    serializer_class = ParroquiaSerializer

class SacerdoteViewSet(viewsets.ModelViewSet):
    queryset = Sacerdote.objects.all()
    serializer_class = SacerdoteSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class SacramentoViewSet(viewsets.ModelViewSet):
    queryset = Sacramento.objects.all()
    serializer_class = SacramentoSerializer

class CelebracionViewSet(viewsets.ModelViewSet):
    queryset = Celebracion.objects.all()
    serializer_class = CelebracionSerializer
