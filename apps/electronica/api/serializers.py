from rest_framework.serializers import ModelSerializer
from apps.electronica.models import Lote, Eras, Sensor
from rest_framework import serializers

class LoteSerializer(ModelSerializer):
    class Meta:
        model = Lote
        fields = ['id', 'nombre', 'descripcion', 'tamX', 'tamY', 'estado', 'posX', 'posY']


class ErasSerializer(ModelSerializer):
    fk_lote = LoteSerializer(read_only=True)
    fk_lote_id = serializers.PrimaryKeyRelatedField(
        queryset=Lote.objects.all(), source='fk_lote', write_only=True
    )

    class Meta:
        model = Eras
        fields = ['id', 'fk_lote', 'fk_lote_id', 'tipo', 'tamX', 'tamY', 'posX', 'posY']


class SensorSerializer(ModelSerializer):
    fk_lote = LoteSerializer(read_only=True)
    fk_lote_id = serializers.PrimaryKeyRelatedField(
        queryset=Lote.objects.all(), source='fk_lote', write_only=True
    )
    tipo_display = serializers.CharField(source='get_tipo_display', read_only=True)

    class Meta:
        model = Sensor
        fields = ['id', 'fk_lote', 'fk_lote_id', 'fecha', 'tipo', 'tipo_display', 'valor']