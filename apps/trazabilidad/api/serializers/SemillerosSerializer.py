from rest_framework.serializers import ModelSerializer
from ..models.SemillerosModel import Semilleros

class SemillerosSerializer(ModelSerializer):
    model = Semilleros
    fields = '__all__'