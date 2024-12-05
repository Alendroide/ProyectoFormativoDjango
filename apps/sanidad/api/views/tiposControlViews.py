from rest_framework.viewsets import ModelViewSet;
from apps.sanidad.api.models.TiposControlModel import TiposControl;
from apps.sanidad.api.serializers.tiposControlSerializer import TiposControlModelSerializer;

class TiposControlModelViewSet(ModelViewSet):
    serializer_class = TiposControlModelSerializer
    queryset = TiposControl.objects.all()