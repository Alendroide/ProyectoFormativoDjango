from rest_framework.serializers import ModelSerializer
from apps.finanzas.api.models.pasantes import Pasantes

class SerializerPasantes(ModelSerializer):
    class Meta:
        model = Pasantes
        fields = "__all__"