from rest_framework.viewsets import ModelViewSet
from apps.finanzas.api.serializers import *
from apps.finanzas.models import *

#modelvieset de tipos de desecho


#modelviewset de cultivos
class ModelViewSetCultivos(ModelViewSet):
    queryset = Cultivos.objects.all()
    serializer_class = SerializerCultivos

#modelviewset de desechos
class ModelViewSetDesechos(ModelViewSet):
    queryset = Desechos.objects.all()
    serializer_class = SerializerDesechos 

#modelviewset de cosechas
class ModelViewSetCosechas(ModelViewSet):
    queryset = Cosechas.objects.all()
    serializer_class = SerializerCosechas 

#modelviewset de ventas
class ModelViewSetVentas(ModelViewSet):
    queryset = Ventas.objects.all()
    serializer_class = SerializerVentas

#modelviewset de actividades
class ModelViewSetActividades(ModelViewSet):
    queryset = Actividades.objects.all()
    serializer_class = SerializerActividades

#modelviewset de insumos
class ModelViewSetInsumos(ModelViewSet):
    queryset = Insumos.objects.all()
    serializer_class = SerializerInsumos 

#modelviewset de usos productos
class ModelViewSetUsosProductos(ModelViewSet):
    queryset = UsosProductos.objects.all()
    serializer_class = SerializerUsosProductos

