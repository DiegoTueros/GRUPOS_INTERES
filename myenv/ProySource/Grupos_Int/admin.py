from django.contrib import admin

# Register your models here.

#from .models import *

from Grupos_Int.models import Universidad
from Grupos_Int.models import Pais
from Grupos_Int.models import Requerimiento
from Grupos_Int.models import Facultad
from Grupos_Int.models import Departamento
from Grupos_Int.models import Autoridad
from Grupos_Int.models import Escuela
from Grupos_Int.models import Provincia
from Grupos_Int.models import Distrito
from Grupos_Int.models import Institucion
from Grupos_Int.models import Perfil
from Grupos_Int.models import PerfilRequerimiento
from Grupos_Int.models import Representante
from Grupos_Int.models import Convenio
from Grupos_Int.models import PlanDeCapacitacion
from Grupos_Int.models import Actividad
from Grupos_Int.models import Objetivo
from Grupos_Int.models import Beneficio
from Grupos_Int.models import Competencia
from Grupos_Int.models import Condicion
from Grupos_Int.models import Horario

admin.site.register(Universidad)
admin.site.register(Pais)
admin.site.register(Requerimiento)
admin.site.register(Facultad)
admin.site.register(Departamento)
admin.site.register(Autoridad)
admin.site.register(Escuela)
admin.site.register(Provincia)
admin.site.register(Distrito)
admin.site.register(Institucion)
admin.site.register(Perfil)
admin.site.register(PerfilRequerimiento)
admin.site.register(Representante)
admin.site.register(Convenio)
admin.site.register(PlanDeCapacitacion)
admin.site.register(Actividad)
admin.site.register(Objetivo)
admin.site.register(Beneficio)
admin.site.register(Competencia)
admin.site.register(Condicion)
admin.site.register(Horario)

