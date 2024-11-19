from rest_framework.serializers import ModelSerializer
from apps.electronica.models import *

class LoteSerializer(ModelSerializer):
    class Meta:
        model = Lote
        fields = '__all__'

class ErasSerializer(ModelSerializer):
    class Meta:
        model = Lote
        fields = '__all__'

class SensorSerializer(ModelSerializer):
    class Meta:
        model = Lote
        fields = '__all__'

class HumedadTerrenoSerializer(ModelSerializer):
    class Meta:
        model = Lote
        fields = '__all__'

class PhSerializer(ModelSerializer):
    class Meta:
        model = Lote
        fields = '__all__'

