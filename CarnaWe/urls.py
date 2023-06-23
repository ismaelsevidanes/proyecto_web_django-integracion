"""CarnaWe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from carnawe_app.views.views_david import mostar_registro
from carnawe_app.views.views_ivan import mostrar_inicio
from carnawe_app.views.views_juanlu import mostrar_ajustesUser
from carnawe_app.views.views_juanlu import cambio_ajustesUser
from carnawe_app.views.views_juanlu import cambio_passwd
from carnawe_app.views.views_daniel import detalleSesion
from carnawe_app.views.views_oscar import mostrar_login
from carnawe_app.views.views_ajota import mostrar_info
from carnawe_app.views.views_ajota import panel_general
from carnawe_app.views.views_ismael import mostrar_compraEntradas
from carnawe_app.views.views_ismael import mostrar_pagoEntradas
from carnawe_app.views.views_ismael import mostrar_loginPago







from carnawe_app.views.views_abraham import usuarios
from carnawe_app.views.views_abraham import agrupaciones
from carnawe_app.views.views_ajota import sesiones
from carnawe_app.views.views_ajota import entradas




urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/', mostar_registro),
    path('', mostrar_inicio),
    path('ajustesUser/',mostrar_ajustesUser),
    path('ajustesUser/cambio_ajusteUser/',cambio_ajustesUser),
    path('ajustesUser/passwd/',cambio_passwd),
    path('detalleSesion/', detalleSesion),
    path('login/', mostrar_login),
    path('informacion/', mostrar_info),
    path('compraEntradas/',mostrar_compraEntradas),
    path('pagoEntradas/',mostrar_pagoEntradas),
    path('loginPago/',mostrar_loginPago),









    path('panel/', panel_general),
    path('panel/usuarios/', usuarios),
    path('panel/agrupaciones/', agrupaciones),
    path('panel/sesiones/', sesiones),
    path('panel/entradas/', entradas)
]
