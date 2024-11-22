from rest_framework.viewsets import ModelViewSet

from apps.sanidad.models import TipoPlaga
from apps.sanidad.api.serializers import TipoPlagaModelSerializer

from apps.sanidad.models import Plaga
from apps.sanidad.api.serializers import PlagaModelSerializer

from apps.sanidad.models import Afecciones
from apps.sanidad.api.serializers import AfeccionesModelSerializer

from apps.sanidad.models import TiposControl
from apps.sanidad.api.serializers import TiposControlModelSerializer

from apps.sanidad.models import Controles
from apps.sanidad.api.serializers import ControlesModelSerializer

from apps.sanidad.models import ProductosControl
from apps.sanidad.api.serializers import ProductosControlModelSerializer

from apps.sanidad.models import UsoProductosControl

from apps.sanidad.api.serializers import UsoProductosControlModelSerializer


class TipoPlagaModelViewSet(ModelViewSet):
    serializer_class = TipoPlagaModelSerializer
    queryset = TipoPlaga.objects.all()
    
class PlagaModelViewSet(ModelViewSet):
    serializer_class = PlagaModelSerializer
    queryset = Plaga.objects.all()
    
class AfeccionesModelViewSet(ModelViewSet):
    serializer_class = AfeccionesModelSerializer
    queryset = Afecciones.objects.all()

class TiposControlModelViewSet(ModelViewSet):
    serializer_class = TiposControlModelSerializer
    queryset = TiposControl.objects.all()
    
class ControleslModelViewSet(ModelViewSet):
    serializer_class = ControlesModelSerializer
    queryset = Controles.objects.all()
    
class ProductosControlModelViewSet(ModelViewSet):
    serializer_class = ProductosControlModelSerializer
    queryset = ProductosControl.objects.all()
    
class UsoProductosControlModelViewSet(ModelViewSet):
    serializer_class = UsoProductosControlModelSerializer
    queryset = UsoProductosControl.objects.all()