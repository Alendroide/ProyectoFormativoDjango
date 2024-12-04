from rest_framework.serializers import ModelSerializer
from ..models.HerramientasModel import Herramientas

class HerramientasSerializer(ModelSerializer):
    model = Herramientas
    fields = '__all__'