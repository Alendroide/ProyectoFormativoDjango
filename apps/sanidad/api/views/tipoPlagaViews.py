from rest_framework.viewsets import ModelViewSet
from apps.sanidad.api.models.tipoPlaga import tipoPlaga
from apps.sanidad.api.serializers.tipoPlagaSerializer import TipoPlagaModelSerializer

class TipoPlagaModelViewSet(ModelViewSet):
    serializer_class = TipoPlagaModelSerializer
    queryset = tipoPlaga.objects.all()