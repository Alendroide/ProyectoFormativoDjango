from rest_framework.viewsets import ModelViewSet
from apps.sanidad.api.models.PlagaModel import Plaga
from apps.sanidad.api.serializers.plagaSerializer import PlagaModelSerializer

class PlagaModelViewSet(ModelViewSet):
    serializer_class = PlagaModelSerializer
    queryset = Plaga.objects.all()