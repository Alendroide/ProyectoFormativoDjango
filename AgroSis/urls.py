"""
URL configuration for AgroSis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#IMPORTACIONES GENERALES
from django.contrib import admin
from django.urls import path,include

#IMPORTACION DE SWAGGER DOCS GENERATOR
from apps.sanidad.api.router import routerSanidad
from apps.finanzas.api.routers.routerActividades import routerActividades
from apps.finanzas.api.routers.routerCosechas import routerCosechas
from apps.finanzas.api.routers.routerCultivos import routerCultivos
from apps.finanzas.api.routers.routerDesechos import routerDesechos
from apps.finanzas.api.routers.routerHorasMensuales import routerHorasMensuales
from apps.finanzas.api.routers.routerInsumos import routerInsumos
from apps.finanzas.api.routers.routerPasantes import routerPasantes
from apps.finanzas.api.routers.routerTiposDesechos import routerTiposDesecho
from apps.finanzas.api.routers.routerUsosProductos import routerUsosProductos
from apps.finanzas.api.routers.routerVentas import routerVentas
from apps.electronica.api.router import routerElectronica
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

#Routers

#Electronica
from apps.electronica.api.routers.era_router import router_era
from apps.electronica.api.routers.lote_router import router_Lote
from apps.electronica.api.routers.sensor_router import router_sensor

#Trazabilidad
from apps.trazabilidad.api.routers.EspeciesRouter import EspeciesRouter
from apps.trazabilidad.api.routers.HerramientasRouter import HerramientasRouter
from apps.trazabilidad.api.routers.PlantacionesRouter import PlantacionesRouter
from apps.trazabilidad.api.routers.SemillerosRouter import SemillerosRouter
from apps.trazabilidad.api.routers.TiposEspeciesRouter import TiposEspecieRouter
from apps.trazabilidad.api.routers.UsosHerramientasRouter import UsosHerramientasRouter

urlpatterns = [
    #SWAGGER Y ADMIN
    path('admin/', admin.site.urls),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    #Routers | EMPEZAR A PARTIR DE ESTA LÍNEA
    
    #Electronica
    path('api/',include(router_era.urls)),
    path('api/',include(router_Lote.urls)),
    path('api/',include(router_sensor.urls)),
    
    #Trazabilidad
    path('api/',include(EspeciesRouter.urls)),
    path('api/',include(TiposEspecieRouter.urls)),
    path('api/',include(HerramientasRouter.urls)),
    path('api/',include(PlantacionesRouter.urls)),
    path('api/',include(SemillerosRouter.urls)),
    path('api/',include(UsosHerramientasRouter.urls)),
    
    path('api/',include(routerSanidad.urls)),
    path('finanzas/api/',include(routerActividades.urls)),
    path('finanzas/api/',include(routerCosechas.urls)),
    path('finanzas/api/',include(routerCultivos.urls)),
    path('finanzas/api/',include(routerDesechos.urls)),
    path('finanzas/api/',include(routerHorasMensuales.urls)),
    path('finanzas/api/',include(routerInsumos.urls)),
    path('finanzas/api/',include(routerPasantes.urls)),
    path('finanzas/api/',include(routerTiposDesecho.urls)),
    path('finanzas/api/',include(routerUsosProductos.urls)),
    path('finanzas/api/',include(routerVentas.urls)),
    path('api/',include(routerElectronica.urls)),
]
