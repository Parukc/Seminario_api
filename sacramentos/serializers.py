from rest_framework import serializers
from .models import *

class DiocesisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diocesis
        fields = '__all__'

class ParroquiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parroquia
        fields = '__all__'

class SacerdoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sacerdote
        fields = '__all__'

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

class SacramentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sacramento
        fields = '__all__'

class CelebracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Celebracion
        fields = '__all__'
