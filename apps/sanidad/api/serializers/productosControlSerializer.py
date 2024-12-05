from rest_framework.serializers import  ModelSerializer;
from apps.sanidad.api.serializers.productosControlSerializer import ProductosControl;

class ProductosControlModelSerializer(ModelSerializer):
    class Meta:
        model = ProductosControl
        fields = "__all__"