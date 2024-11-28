from rest_framework.serializers import ModelSerializer
from ..models.UsosHerramientasModel import UsosHerramientas

class UsosHerramientasSerializer(ModelSerializer):
    model = ModelSerializer
    fields = '__all__'