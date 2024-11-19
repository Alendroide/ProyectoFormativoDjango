from rest_framework.viewsets import ModelViewSet
from apps.electronica.models import *
from apps.electronica.api.serializers import *

class LoteView(ModelViewSet):
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer

class Erasview(ModelViewSet):
    queryset = Eras.objects.all()
    serializer_class = ErasSerializer

class sensoresview(ModelViewSet):
    queryset =Sensor.objects.all()
    serializer_class = SensorSerializer

class HumedadTerrenoview(ModelViewSet):
    queryset = HumedadTerreno.objects.all()
    serializer_class = HumedadTerrenoSerializer

class Phview(ModelViewSet):
    queryset = PH.objects.all()
    serializer_class = PhSerializer