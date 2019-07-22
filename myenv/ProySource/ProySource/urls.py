"""ProySource URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path
from Grupos_Int import views
from Grupos_Int.views import ConvenioList,ConvenioCreate,ConvenioUpdate,ConvenioDelete
from Grupos_Int.views import InstitucionList, InstitucionCreate, InstitucionUpdate, InstitucionDelete
from Grupos_Int.views import PlanCapList, PlanCapCreate, PlanCapUpdate, PlanCapDelete
from Grupos_Int.views import CompetenciasList
from Grupos_Int.views import PerfilRequerList, PerfilRequerCreate,PerfilRequerUpdate,PerfilRequerDelete
#from Grupos_Int.views import CondicionList

from Grupos_Int.views import GIList
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='Inicio'),
    path('principal', views.principal, name='principal'),
    path('GI', GIList.as_view(), name='GI' ),


    #URL instituciones
    path('instituciones/consultar', InstitucionList.as_view(), name='instituciones' ),
    path('instituciones/Crear', InstitucionCreate.as_view(), name='Inst_Form'),
    re_path(r'^instituciones/Editar/(?P<pk>\d+)/$', InstitucionUpdate.as_view(), name='Inst_edit'),
    re_path(r'^instituciones/Eliminar/(?P<pk>\d+)/$', InstitucionDelete.as_view(), name='Inst_delete'),
    #URL convenios
    path('convenios/consultar', ConvenioList.as_view(), name='convenios'),
    path('convenios/Crear', ConvenioCreate.as_view(), name='Conv_Form'),
    re_path(r'^convenios/Editar/(?P<pk>\d+)/$', ConvenioUpdate.as_view(), name='Conv_edit'),
    re_path(r'^convenios/Eliminar/(?P<pk>\d+)/$', ConvenioDelete.as_view(), name='Conv_delete'),
    #URL plan de capacitacion
    path('Inicio_PlanCap', views.inicioPC, name='Inicio_PlanCap'),
    path('plan_cap', PlanCapList.as_view(), name='plan_cap'),
    path('PlanCap_Form', PlanCapCreate.as_view(), name='PlanCap_Form'),
    re_path(r'^PlanCap_edit/(?P<pk>\d+)/$', PlanCapUpdate.as_view(), name='PlanCap_edit'),
    re_path(r'^PlanCap_delete/(?P<pk>\d+)/$', PlanCapDelete.as_view(), name='PlanCap_delete'),
    #URL competencia
    path('capacitacion/competencias/consultar', CompetenciasList.as_view(), name='Competencias' ),
    #URL Perfil_Requerimiento
    path('instituciones/perfil_requerimiento/consultar', PerfilRequerList.as_view(), name='PerfilRequer' ),
    path('instituciones/perfil_requerimiento/Crear', PerfilRequerCreate.as_view(), name='PerfilRequer_Form'),
    re_path(r'^instituciones/perfil_requerimiento/Editar/(?P<pk>\d+)/$', PerfilRequerUpdate.as_view(), name='PerfilRequer_Edit'),
    re_path(r'^instituciones/perfil_requerimiento/Eliminar/(?P<pk>\d+)/$', PerfilRequerDelete.as_view(), name='PerfilRequer_delete'),
    
]
