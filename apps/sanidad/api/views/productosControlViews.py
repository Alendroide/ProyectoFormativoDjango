from rest_framework.viewsets import ModelViewSet
from apps.sanidad.api.models.ProductosControlModel import ProductosControl
from apps.sanidad.api.serializers.productosControlSerializer import ProductosControlModelSerializer

class ProductosControlModelViewSet(ModelViewSet):
    serializer_class = ProductosControlModelSerializer
    queryset = ProductosControl.objects.all()