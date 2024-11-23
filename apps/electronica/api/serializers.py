from rest_framework.serializers import ModelSerializer
from apps.electronica.models import *
from rest_framework import serializers

class LoteSerializer(ModelSerializer):
    class Meta:
        model = Lote
        fields = ['id', 'nombre','descripcion','tamX','tamY','estado','posX','posY']

class ErasSerializer(ModelSerializer):
    fk_lote = LoteSerializer(read_only=True)
    fk_lote_id = serializers.PrimaryKeyRelatedField(
        queryset = Lote.objects.all(),source = 'fk_lote', write_only=True 
    )
    class Meta:
        model = Eras
        fields = ['id','fk_lote','tipo','fk_lote_id', 'nombre','descripcion','tamX','tamY','posX','posY']

class SensorSerializer(ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'


