from rest_framework.viewsets import ModelViewSet;
from apps.sanidad.api.serializers.controlesSerializer import ControlesModelSerializer;
from apps.sanidad.api.models.controlesModel import Controles;

class ControleslModelViewSet(ModelViewSet):
    serializer_class = ControlesModelSerializer
    queryset = Controles.objects.all()