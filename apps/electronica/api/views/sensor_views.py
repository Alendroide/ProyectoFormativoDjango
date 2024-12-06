from rest_framework.viewsets import ModelViewSet
from apps.electronica.api.models.sensor import *
from apps.electronica.api.serializers.Sensor_Serializer import *

class sensoresview(ModelViewSet):
    queryset =Sensor.objects.all()
    serializer_class = SensorSerializer