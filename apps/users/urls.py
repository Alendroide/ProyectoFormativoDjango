from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet

router = DefaultRouter()

router.register(prefix='usuarios',viewset=UsuarioViewSet,basename='usuarios')