from rest_framework.viewsets import ModelViewSet;
from apps.sanidad.api.models.UsoProductosControlModel import UsoProductosControl;
from apps.sanidad.api.serializers.usosProductosControlSerializer import UsoProductosControlModelSerializer;

class UsoProductosControlModelViewSet(ModelViewSet):
    serializer_class = UsoProductosControlModelSerializer
    queryset = UsoProductosControl.objects.all()