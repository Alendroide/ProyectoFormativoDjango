from rest_framework.serializers import ModelSerializer
from apps.finanzas.models import *

#serializer tipo de desechos
class SerializerTiposDesecho(ModelSerializer):
    class Meta:
        model = TiposDesecho
        fields = '__all__'

#serializer cultivos.
class SerializerCultivos(ModelSerializer):
    class Meta:
        model = Cultivos
        fields = '__all__'

#serializer desechos.
class SerializerDesechos(ModelSerializer):
    class Meta:
        model = Desechos
        fields = '__all__'

#serializer cosechas.

#serializer ventas.
class SerializerVentas(ModelSerializer):
    class Meta:
        model = Ventas
        fields = '__all__'

#serializer activiades.


#serializer insumos.
class SerializerInsumos(ModelSerializer):
    class Meta:
        model = Insumos
        fields = '__all__'

#serializer usos de productos.
class SerializerUsosProductos(ModelSerializer):
    class Meta:
        model = UsosProductos
        fields = '__all__'