"""
URL configuration for misitio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from misitio.views import *
from cerveceria.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler400, handler500

handler400 = error_404
handler500 = error_500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola/' , hola),
    path('ahora' , fecha_actual),
    path('ahora/mas/<int:offset>/' , horas_adelante),
    path('aleatorio/' , aleatorio),
    path('semana' , semana),
    path('',index, name='inicio'),
    path('somos/', somos, name='somos'),
    path('busqueda/', buscar, name='busqueda'),
    path('contacto/', contacto, name='contacto'),
    path('registro/', usuario_nuevo, name='registro'),
    path('ingresar/', ingresar, name='ingresar'),
    path('privado/', privado, name='privado'),
    path('salir/', salir, name='salir'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
