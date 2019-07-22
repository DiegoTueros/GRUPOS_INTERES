from django import forms
from .models import Universidad, Institucion, Convenio, PlanDeCapacitacion
from .models import Pais, Requerimiento, Facultad, Departamento, Autoridad
from .models import Escuela, Provincia, Distrito, Perfil, PerfilRequerimiento
from .models import Representante, Actividad, Beneficio, Competencia
from .models import Condicion, Objetivo

class UniversidadForm(forms.ModelForm):

    class Meta:
        model = Universidad

        fields = [
            'nombre',
        ]
        labels = {
            'nombre': 'Nombre Universidad',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PaisForm(forms.ModelForm):

    class Meta:
        model = Pais

        fields = [
            'nombre',
        ]
        labels = {
            'nombre': 'Pais',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }

class RequerimientoForm(forms.ModelForm):

    class Meta:
        model = Requerimiento

        fields = [
            'nombre',
            'descripcion',
            'area',
        ]
        labels = {
            'nombre': 'Requermiento',
            'descripcion': 'Descripción',
            'area': 'Area',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'area': forms.TextInput(attrs={'class': 'form-control'}),
        } 

class FacultadForm(forms.ModelForm):

    class Meta:
        model = Facultad

        fields = [
            'universidad',
        ]
        labels = {
            'universidad': 'Universidad',
        }

        widgets = {
            'universidad': forms.Select(attrs={'class': 'form-control'}),
        }

class DepartamentoForm(forms.ModelForm):

    class Meta:
        model = Departamento

        fields = [
            'pais',
        ]
        labels = {
            'pais': 'Pais',
        }

        widgets = {
            'pais': forms.Select(attrs={'class': 'form-control'}),
        }

class AutoridadForm(forms.ModelForm):

    class Meta:
        model = Autoridad

        fields = [
            'nombres',
            'apellidoPaterno',
            'apellidoMaterno',
            'correo',
            'telefono',
            'cargo',
            'grado',
            'dni',
            ]
        labels = {
            'nombre': 'Nombres',
            'apellidoPaterno': 'Apellido Paterno',
            'apellidoMaterno': 'Apellido Materno',
            'correo': 'Correo',
            'telefono': 'Telefono',
            'cargo': 'Cargo',
            'grado': 'Grado',
            'dni': 'Dni',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidoPaterno': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidoMaterno': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control'}),
            'grado': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
        
        }

class EscuelaForm(forms.ModelForm):

    class Meta:
        model = Escuela

        fields = [
            'facultad',
        ]
        labels = {
            'facultad': 'Facultad',
        }

        widgets = {
            'facultad': forms.Select(attrs={'class': 'form-control'}),
        }

class ProvinciaForm(forms.ModelForm):

    class Meta:
        model = Provincia

        fields = [
            'departamento',
        ]
        labels = {
            'departamento': 'Departamento',
        }

        widgets = {
            'departamento': forms.Select(attrs={'class': 'form-control'}),
        }

class DistritoForm(forms.ModelForm):

    class Meta:
        model = Distrito

        fields = [
            'provincia',
        ]
        labels = {
            'provincia': 'Provincia',
        }

        widgets = {
            'provincia': forms.Select(attrs={'class': 'form-control'}),
        }

class InstitucionesForm(forms.ModelForm):

    class Meta:
        model = Institucion

        fields = [
            'nombre',
            'tipo',
            'descripcion',
            'paginaWeb',
            'direccion',
            'ruc',
            'distrito',
        ]
        labels = {
            'nombre': 'Nombre',
            'tipo': 'Tipo',
            'descripcion': 'Descripción',
            'paginaWeb': 'Pagina Web',
            'direccion': 'Dirección',
            'ruc': 'RUC',
            'distrito': 'Distrito',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'paginaWeb': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'ruc': forms.TextInput(attrs={'class': 'form-control'}),
            'distrito': forms.Select(attrs={'class': 'form-control'}),
        }

class PerfilForm(forms.ModelForm):

    class Meta:
        model = Perfil

        fields = [
            'institucion',
            'descripcion',
        ]
        labels = {
            'institucion': 'Institucion',
            'descripcion': 'Perfil',
        }

        widgets = {
            'institucion': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PerfilRequerimientoForm(forms.ModelForm):

    class Meta:
        model = PerfilRequerimiento

        fields = [
            'prioridad',
        ]
        labels = {
            'prioridad': 'Prioridad',
        }

        widgets = {
            'prioridad': forms.TextInput(attrs={'class': 'form-control'}),

        }

class RepresentanteForm(forms.ModelForm):

    class Meta:
        model = Representante

        fields = [
            'nombres',
            'apellidoPaterno',
            'apellidoMaterno',
            'correo',
            'telefono',
            'cargo',
            'area',
            'dni',
            ]
        labels = {
            'nombres': 'Nombres',
            'apellidoPaterno': 'Apellido Paterno',
            'apellidoMaterno': 'Apellido Materno',
            'correo': 'Correo',
            'telefono': 'Telefono',
            'cargo': 'Cargo',
            'grado': 'Grado',
            'dni': 'Dni',
        }

        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidoPaterno': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidoMaterno': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control'}),
            'area': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
        
        }

class ConveniosForm(forms.ModelForm):

    class Meta:
        model = Convenio

        fields = [
            'escuela',
            'institucion',
            'nombre',
            'tipo',
            'fechaInicio',
            'fechaFin',
        ]
        labels = {
            'escuela': 'Escuela',
            'institucion': 'Institucion',
            'nombre': 'Nombre',
            'tipo': 'Tipo',
            'fechaInicio': 'Fecha Inicial',
            'fechaFin': 'Fecha Final',
        }

        widgets = {
            'escuela': forms.Select(attrs={'class': 'form-control'}),
            'institucion': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'fechaInicio': forms.DateInput(attrs={'class': 'form-control'}),
            'fechaFin': forms.DateInput(attrs={'class': 'form-control'}),

        }

class PlanCapForm(forms.ModelForm):

    class Meta:
        model = PlanDeCapacitacion

        fields = [
            'denominacion',
        ]
        labels = {
            'denominacion': 'Denominación',
        }

        widgets = {
            'denominacion': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ActividadForm(forms.ModelForm):

    class Meta:
        model = Actividad

        fields = [
            'funcionPrincipal',
            'tareasDerivadas',
            'capacitacion',
        ]
        labels = {
            'funcionPrincipal': 'Función',
            'tareasDerivadas': 'Tareas',
            'capacitacion': 'Plan de Capacitación',
        }

        widgets = {
            'funcionPrincipal': forms.TextInput(attrs={'class': 'form-control'}),
            'tareasDerivadas': forms.TextInput(attrs={'class': 'form-control'}),
            'capacitacion': forms.Select(attrs={'class': 'form-control'}),
        }

class BeneficioForm(forms.ModelForm):

    class Meta:
        model = Beneficio

        fields = [
            'descripcion',
            'beneficiado',
        ]
        labels = {
            'descripcion': 'Descripción',
            'beneficiado': 'Beneficiado',
        }

        widgets = {
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'beneficiado': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CompetenciaForm(forms.ModelForm):

    class Meta:
        model = Competencia

        fields = [
            'compEspecificas',
            'compGenericas',
            'capacitacion',
        ]
        labels = {
            'compEspecificas': 'Competencias Especificas',
            'compGenericas': 'Competencias Genericas',
            'capacitacion': 'Plan de Capacitación',
        }

        widgets = {
            'compEspecificas': forms.Textarea(attrs={'class': 'form-control'}),
            'compGenericas': forms.Textarea(attrs={'class': 'form-control'}),
            'capacitacion': forms.Select(attrs={'class': 'form-control'}),
        } 

class CondicionForm(forms.ModelForm):

    class Meta:
        model = Condicion

        fields = [
            'monto',
            'tipoSeguroCobertura',
            'ocupacion',
        ]
        labels = {
            'monto': 'Monto de la Subención',
            'tipoSeguroCobertura': 'Tipo de seguro y cobertura',
            'ocupacion': 'Ocupación',
        }

        widgets = {
            'monto': forms.TextInput(attrs={'class': 'form-control'}),
            'tipoSeguroCobertura': forms.TextInput(attrs={'class': 'form-control'}),
            'ocupacion': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ObjetivoForm(forms.ModelForm):

    class Meta:
        model = Objetivo

        fields = [
            'nombre',
            'descripcion',
            'capacitacion',
        ]
        labels = {
            'nombre': 'Obejetivo',
            'descripcion': 'Descripción',
            'capacitacion': 'Plan de Capacitación',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'capacitacion': forms.Select(attrs={'class': 'form-control'}),
        }           

'''class HorarioForm(forms.ModelForm):

    class Meta:
        model = Horario

        fields = [
            'dias_trabajar',
            'minimo_horas',
            'maximo_horas',
            'hora_salida',
            'hora_entrada',
        ]
        labels = {
            'dias_trabajar': 'Días de Trabajo',
            'minimo_horas': 'Minimo de horas',
            'maximo_horas': 'Maximo de horas',
            'hora_salida': 'Hora de Salida',
            'hora_entrada': 'Hora de Entrada',
        }

        widgets = {
            'dias_trabajar': forms.TextInput(attrs={'class': 'form-control'}),
            'minimo_horas': forms.TextInput(attrs={'class': 'form-control'}),
            'maximo_horas': forms.TextInput(attrs={'class': 'form-control'}),
            'hora_salida': forms.TimeInput(attrs={'class': 'form-control'}),
            'hora_entrada': forms.TimeInput(attrs={'class': 'form-control'}),       
        }'''