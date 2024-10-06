"""
URL configuration for ProyectoCoopApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from ProyectoCoopApp.views.inicio import index
from ProyectoCoopApp.views.registro import registro, formulario_registro
from ProyectoCoopApp.views.login import  login
from ProyectoCoopApp.views.logout import logout_user
from ProyectoCoopApp.views.simulaCredito import credito, formulario_credito, guardar_evaluacion_credito
from ProyectoCoopApp.views.evaluacionCredito import  cargaEvaluacion, evaluacionCredito
from ProyectoCoopApp.views.resultados import resultado, exportar_evaluaciones_excel
from ProyectoCoopApp.views.panel import panel
from ProyectoCoopApp.views import errorpage
from django.contrib.auth.models import Permission ,ContentType
from django.urls import path





urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('', index),
    # llamar a pagina registro y la funcion que ingresa datos -> formulario_registro
    path('registro/', registro),
    path('registro/formulario', formulario_registro),
    # formulario de login
    path('login/', login),
   # path('login/', login_index), 
    path('logout/', logout_user),
    path('error-401/', errorpage.error_401_page),
    path('error-403/', errorpage.error_403_page),
    # simulacion de credito
    path('simulaCredito/', credito),
    path('simulaCredito/formulario', formulario_credito),
    path('simulaCredito/formulario2', guardar_evaluacion_credito),
    # simulacion de credito
    path('evaluacionCredito/', evaluacionCredito),
    path('evaluacionCredito/formulario', cargaEvaluacion),
    #Resultados
    path('resultados/', resultado),
    path('resultados/exportar_excel/', exportar_evaluaciones_excel, name='exportar_evaluaciones_excel'),
    #Panle
    path('panel/', panel),
    

    
]
