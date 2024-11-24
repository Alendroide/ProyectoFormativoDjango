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

from django.contrib import admin
from django.urls import path, include
from apps.sanidad.api.router import router_tipoPlaga
from apps.sanidad.api.router import router_plaga
from apps.sanidad.api.router import router_afecciones
from apps.sanidad.api.router import router_tiposControl
from apps.sanidad.api.router import router_controles
from apps.sanidad.api.router import router_productosControl
from apps.sanidad.api.router import router_usoProductosControl


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router_tipoPlaga.urls)),
    path("api/", include(router_plaga.urls)),
    path("api/", include(router_afecciones.urls)),
    path("api/", include(router_tiposControl.urls)),
    path("api/", include(router_controles.urls)),
    path("api/", include(router_productosControl.urls)),
    path("api/", include(router_usoProductosControl.urls)),
]
