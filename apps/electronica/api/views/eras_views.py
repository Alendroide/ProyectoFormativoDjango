from rest_framework.viewsets import ModelViewSet
from apps.electronica.api.models.era import *
from apps.electronica.api.serializers.Eras_Seralizer import *

class Erasview(ModelViewSet):
    queryset = Eras.objects.all()
    serializer_class = ErasSerializer