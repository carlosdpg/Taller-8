"""registro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from aplicacion.principal.views import get_data_for_columns
from aplicacion.principal.class_view import PersonaList, PersonaCreate, PersonaUpdate,PersonaDelete, CiudadList, CiudadCreate, CiudadUpdate, CiudadDelete, TipoDocumentoList, TipoDocumentoCreate, TipoDocumentoUpdate, TipoDocumentoDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_data_for_columns, name = 'index'),

    #path('',PersonaList.as_view(),name = "ver_personas"),
    path('crear_persona.html/',PersonaCreate.as_view(),name = 'crear_persona'),
    path('editar_persona/<int:pk>/',PersonaUpdate.as_view(),name = 'editar_persona'),
    path('eliminar_persona/<int:pk>/', PersonaDelete.as_view(), name = 'eliminar_persona'),

    #path('',CiudadList.as_view(),name = "ver_ciudades"),
    path('crear_ciudad.html/',CiudadCreate.as_view(),name = 'crear_ciudad'),
    path('editar_ciudad/<int:pk>/',CiudadUpdate.as_view(),name = 'editar_ciudad'),
    path('eliminar_ciudad/<int:pk>/', CiudadDelete.as_view(), name = 'eliminar_ciudad'),

    #path('',TipoDocumentoList.as_view(),name = "ver_tipodocumentos"),
    path('crear_tipodocumento.html/',TipoDocumentoCreate.as_view(),name = 'crear_tipodocumento'),
    path('editar_tipodocumento/<int:pk>/',TipoDocumentoUpdate.as_view(),name = 'editar_tipodocumento'), 
    path('eliminar_tipodocumento/<int:pk>/', TipoDocumentoDelete.as_view(), name = 'eliminar_tipodocumento'),  
]
