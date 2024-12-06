from rest_framework.serializers import ModelSerializer
from ..models.PlantacionesModel import Plantaciones

class PlantacionesSerializer(ModelSerializer):
    model = Plantaciones
    fields = '__all__'