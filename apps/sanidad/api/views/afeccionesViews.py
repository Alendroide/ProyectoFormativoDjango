from rest_framework.viewsets import ModelViewSet;
from apps.sanidad.api.models.AfeccionesMoldel import Afecciones;
from apps.sanidad.api.serializers.afeccionesSerializer import AfeccionesModelSerializer;

class AfeccionesModelViewSet(ModelViewSet):
    serializer_class = AfeccionesModelSerializer
    queryset = Afecciones.objects.all()