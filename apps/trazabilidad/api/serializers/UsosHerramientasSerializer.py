from rest_framework.serializers import ModelSerializer
from ..models.UsosHerramientasModel import UsosHerramientas

class UsosHerramientasSerializer(ModelSerializer):
    model = UsosHerramientas
    fields = '__all__'