"""Balastrera URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #Tierra
    url(r'^tierra/listado/$', 'tierra.views.listadoTierra', name='tierra_listado'),
    url(r'^tierra/ingresar/$', 'tierra.views.ingresarTierra', name='tierra_ingresar'),
    url(r'^$', 'tierra.views.inicio', name='inicio'),
    url(r'^tierra/eliminar/(?P<id_t>\d+)$', 'tierra.views.eliminarTierra', name='tierra_eliminar'),
    url(r'^tierra/editar/(?P<id_t>\d+)$', 'tierra.views.editarTierra', name='editar_tierras'),
    #Volco
    url(r'^volco/listado/$', 'volco.views.listadoVolco', name='volco_listado'),
    url(r'^volco/ingresar/$', 'volco.views.ingresarVolco', name='volco_ingresar'),
    url(r'^volco/eliminar/(?P<id_v>\d+)$', 'volco.views.eliminarVolco', name='volco_eliminar'),
    url(r'^volco/editar/(?P<id_v>\d+)$', 'volco.views.editarVolco', name='editar_volco'),
    #Venta
    url(r'^venta/listado/$', 'venta.views.listadoVenta', name='venta_listado'),
    url(r'^venta/ingresar/$', 'venta.views.ingresarVenta', name='venta_ingresar'),
    url(r'^venta/eliminar/(?P<id_v>\d+)$', 'venta.views.eliminarVenta', name='venta_eliminar'),
    #Maquina
    url(r'^maquina/listado/$', 'maquina.views.listadoMaquina', name='maquina_listado'),
    url(r'^maquina/ingresar/$', 'maquina.views.ingresarMaquina', name='maquina_ingresar'),
    url(r'^maquina/eliminar/(?P<id_m>\d+)$', 'maquina.views.eliminarMaquina', name='maquina_eliminar'),
    url(r'^maquina/editar/(?P<id_m>\d+)$', 'maquina.views.editarMaquina', name='editar_eliminar'),

]
