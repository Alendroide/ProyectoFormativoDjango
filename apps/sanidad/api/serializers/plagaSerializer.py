from rest_framework.serializers import ModelSerializer
from apps.sanidad.api.models.PlagaModel import Plaga;
from apps.sanidad.api.serializers.tipoPlagaSerializer import TipoPlagaModelSerializer;


class PlagaModelSerializer(ModelSerializer):
    tipoPlaga = TipoPlagaModelSerializer(read_only=True)
    class Meta:
        model = Plaga
        fields = "__all__"