from rest_framework.serializers import ModelSerializer
from apps.sanidad.models import TipoPlaga
from apps.sanidad.models import Plaga
from apps.sanidad.models import Afecciones
from apps.sanidad.models import TiposControl
from apps.sanidad.models import Controles
from apps.sanidad.models import ProductosControl
from apps.sanidad.models import UsoProductosControl

class TipoPlagaModelSerializer(ModelSerializer):
    class Meta:
        model = TipoPlaga
        fields = '__all__'
        
class PlagaModelSerializer(ModelSerializer):
    class Meta:
        model = Plaga
        fields = '__all__'
        
class AfeccionesModelSerializer(ModelSerializer):
    class Meta:
        model = Afecciones
        fields = '__all__'
        
class TiposControlModelSerializer(ModelSerializer):
    class Meta:
        model = TiposControl
        fields = '__all__'
        

class ControlesModelSerializer(ModelSerializer):
    class Meta: 
        model = Controles      
        fields = '__all__'
        
class ProductosControlModelSerializer(ModelSerializer):
    class Meta: 
        model = ProductosControl      
        fields = '__all__'
        
class UsoProductosControlModelSerializer(ModelSerializer):
    class Meta: 
        model = UsoProductosControl      
        fields = '__all__'