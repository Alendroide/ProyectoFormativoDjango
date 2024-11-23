from rest_framework.viewsets import ModelViewSet
from apps.electronica.api.models.lote import *
from apps.electronica.api.serializers.Lote_Serializer import *

class LoteView(ModelViewSet):
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer