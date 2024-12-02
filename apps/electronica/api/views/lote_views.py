from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from apps.electronica.api.models.lote import Lote
from apps.electronica.api.models.sensor import Sensor
from apps.electronica.api.serializers.Lote_Serializer import LoteSerializer
import math

class LoteView(ModelViewSet):

    queryset = Lote.objects.all()
    serializer_class = LoteSerializer

    @action(detail=True, methods=['get'])
    def calcular_evapotranspiracion(self, request, pk=None):
        try:
            lote = self.get_object()
            evapotranspiracion = self._calcular_evapotranspiracion(lote)

            return Response(
                {"lote": lote.nombre, "evapotranspiracion": evapotranspiracion},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def _calcular_evapotranspiracion(self, lote):
        try:

            temperatura = self._obtener_ultimo_valor(lote, 'TEM')
            humedad_relativa = self._obtener_ultimo_valor(lote, 'HUM_A')
            radiacion_solar = self._obtener_ultimo_valor(lote, 'LUM')
            velocidad_viento = self._obtener_ultimo_valor(lote, 'VIE')

            velocidad_viento = velocidad_viento * 1000 / 3600  
            radiacion_solar = radiacion_solar * 0.0864  

            elevacion = 1000  
            es = 0.6108 * math.exp((17.27 * temperatura) / (temperatura + 237.3))
            ea = es * (humedad_relativa / 100)
            delta = (4098 * es) / ((temperatura + 237.3) ** 2)
            gamma = 0.665 * 10 ** -3 * (101.3 * ((293 - (0.0065 * elevacion)) / 293) ** 5.26)

            ET0 = (0.408 * delta * radiacion_solar +
                   gamma * (900 / (temperatura + 273)) * velocidad_viento * (es - ea)) / \
                  (delta + gamma * (1 + 0.34 * velocidad_viento))

            return round(ET0, 2)
        except ValueError as e:
            return str(e)
        except Exception as e:
            return f"Error inesperado: {str(e)}"

    def _obtener_ultimo_valor(self, lote, tipo_sensor):
        sensor = lote.sensores.filter(tipo=tipo_sensor).order_by('-fecha').first()
        if not sensor:
            raise ValueError(f"No se encontró un sensor de tipo '{tipo_sensor}' asociado al lote.")
        return sensor.valor