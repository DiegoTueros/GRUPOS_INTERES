from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from .models import Convenio, Escuela, Facultad, Universidad
from .models import PlanDeCapacitacion, Competencia, Objetivo, Actividad
from .models import Representante,Institucion,Distrito,Provincia,Departamento
from .models import Perfil,PerfilRequerimiento,Requerimiento
from .models import  Condicion
from Grupos_Int.forms import InstitucionesForm, RepresentanteForm,DistritoForm, ProvinciaForm,DepartamentoForm,PaisForm
from Grupos_Int.forms import ConveniosForm, UniversidadForm, EscuelaForm, FacultadForm
from Grupos_Int.forms import PlanCapForm
from Grupos_Int.forms import RequerimientoForm, PerfilRequerimientoForm, PerfilForm
# Create your views here.

#prueba 
def prueba(request):
    return render(request, "tables.html", {})
    

#-----------------#
#Grupos de Interes
#-----------------#
# Pagina Principal

def inicio(request):
    return render(request, "inicio.html", {})


def principal(request):
    return render(request, "principal.html", {})

#Listar
class GIList (ListView):
    model = Convenio
    template_name = 'GrupoInteres_List.html'

#-------------#
#Instituciones
#-------------#
    
# Listar
class InstitucionList (ListView):
    model = Representante
    template_name = 'instituciones_List.html'

# Registrar
class InstitucionCreate (CreateView):
    model = Representante
    form_class = RepresentanteForm
    second_form_class = InstitucionesForm
    thir_form_class = DistritoForm
    fourth_form_class = ProvinciaForm
    fifth_form_class = DepartamentoForm
    template_name = "instituciones_Form.html"
    success_url = reverse_lazy ("instituciones")

    def get_context_data(self, **kwargs):
        context = super (InstitucionCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        if 'form3' not in context:
            context['form3'] = self.thir_form_class(self.request.GET)
        if 'form4' not in context:
            context['form4'] = self.fourth_form_class(self.request.GET)
        if 'form5' not in context:
            context['form5'] = self.fifth_form_class(self.request.GET)
        return context

    def post (self, request, *args, **kargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        form3 = self.thir_form_class(request.POST)
        form4 = self.fourth_form_class(request.POST)
        form5 = self.fifth_form_class(request.POST)
        if form.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid():
            R = form.save(commit=False)
            R.institucion = form2.save()
            R.institucion.distrito =form3.save()
            R.institucion.distrito.provincia =form4.save()
            R.institucion.distrito.provincia.departamento =form5.save()
            R.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form,form2=form2,form3=form3,form4=form4,form5=form5))

# Modificar
class InstitucionUpdate (UpdateView):
    model = Representante
    second_model =Institucion
    thir_model = Distrito
    fourth_model = Provincia
    fifth_model = Departamento
    template_name = "instituciones_Form.html"
    form_class = RepresentanteForm
    second_form_class = InstitucionesForm
    thir_form_class = DistritoForm
    fourth_form_class = ProvinciaForm
    fifth_form_class = DepartamentoForm
    success_url = reverse_lazy ("instituciones")

    def get_context_data (self, **kwargs):
        context = super(InstitucionUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        Representante = self.model.objects.get(id=pk)
        Institucion = self.second_model.objects.get(id=Representante.institucion_id)
        Distrito = self.thir_model.objects.get(id=Representante.institucion.distrito_id)
        Provincia = self.fourth_model.objects.get(id=Representante.institucion.distrito.provincia_id)
        Departamento = self.fifth_model.objects.get(id=Representante.institucion.distrito.provincia.departamento_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance = Representante.institucion)
        if 'form3' not in context:
            context['form3'] = self.thir_form_class(instance = Representante.institucion.distrito)
        if 'form4' not in context:
            context['form4'] = self.fourth_form_class(instance = Representante.institucion.distrito.provincia)
        if 'form5' not in context:
            context['form5'] = self.fifth_form_class(instance = Representante.institucion.distrito.provincia.departamento)
        context ['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_Representante = kwargs['pk']
        Representante = self.model.objects.get(id=id_Representante)
        Institucion = self.second_model.objects.get(id=Representante.institucion_id)
        Distrito = self.thir_model.objects.get(id=Representante.institucion.distrito_id)
        Provincia = self.fourth_model.objects.get(id=Representante.institucion.distrito.provincia_id)
        Departamento = self.fifth_model.objects.get(id=Representante.institucion.distrito.provincia.departamento_id)
        form = self.form_class(request.POST, instance = Representante)
        form2 = self.second_form_class(request.POST, instance = Institucion)
        form3 = self.thir_form_class(request.POST, instance = Distrito)
        form4 = self.fourth_form_class(request.POST, instance = Provincia)
        form5 = self.fifth_form_class(request.POST, instance = Departamento)
        if form.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid():
            form.save()
            form2.save()
            form3.save()
            form4.save()
            form5.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())
# Eliminar

class InstitucionDelete (DeleteView):
    model = Representante
    template_name = "instituciones_delete.html"
    success_url = reverse_lazy ("instituciones")
#---------#
#Convenios
#---------#

#Listar

class ConvenioList (ListView):
    model = Convenio
    template_name = 'convenios_List.html'
#Registrar

class ConvenioCreate (CreateView):
    model = Convenio
    form_class = ConveniosForm
    second_form_class = EscuelaForm
    thir_form_class = FacultadForm
    template_name = "convenios_Form.html"
    success_url = reverse_lazy ("convenios")

    def get_context_data(self, **kwargs):
        context = super (ConvenioCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        if 'form3' not in context:
            context['form3'] = self.thir_form_class(self.request.GET)
        return context

    def post (self, request, *args, **kargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        form3 = self.thir_form_class(request.POST)
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            R = form.save(commit=False)
            R.escuela = form2.save()
            R.escuela.facultad =form3.save()
            R.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form,form2=form2,form3=form3))


#Modificar

class ConvenioUpdate (UpdateView):
    model = Convenio
    second_model =Escuela
    thir_model = Facultad
    template_name = "convenios_Form.html"
    form_class = ConveniosForm
    second_form_class = EscuelaForm
    thir_form_class = FacultadForm
    success_url = reverse_lazy ("convenios")

    def get_context_data (self, **kwargs):
        context = super(ConvenioUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        Convenio = self.model.objects.get(id=pk)
        Escuela = self.second_model.objects.get(id=Convenio.escuela_id)
        Facultad = self.thir_model.objects.get(id=Convenio.escuela.facultad_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance = Convenio.escuela)
        if 'form3' not in context:
            context['form3'] = self.thir_form_class(instance = Convenio.escuela.facultad)
        context ['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_Convenio = kwargs['pk']
        Convenio = self.model.objects.get(id=id_Convenio)
        Escuela = self.second_model.objects.get(id=Convenio.escuela_id)
        Facultad = self.thir_model.objects.get(id=Convenio.escuela.facultad_id)
        form = self.form_class(request.POST, instance = Convenio)
        form2 = self.second_form_class(request.POST, instance = Escuela)
        form3 = self.thir_form_class(request.POST, instance = Facultad)
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            form.save()
            form2.save()
            form3.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())
#Eliminar

class ConvenioDelete (DeleteView):
    model = Convenio
    template_name = "Convenios_delete.html"
    success_url = reverse_lazy ("convenios")

#Plan de Capacitación 
# Pagina Principal 

def inicioPC(request):
    return render(request, "plan_cap_inicio.html", {})
# Listar
class PlanCapList (ListView):
    model = PlanDeCapacitacion
    template_name = "plan_cap_List.html"

# Registrar
class PlanCapCreate (CreateView):
    model = PlanDeCapacitacion
    form_class = PlanCapForm
    template_name = 'plan_cap_Form.html'
    success_url = reverse_lazy ("plan_cap")

# Modificar

class PlanCapUpdate (UpdateView):
    model = PlanDeCapacitacion
    form_class = PlanCapForm
    template_name = 'plan_cap_Form.html'
    success_url = reverse_lazy ("plan_cap")

# Eliminar

class PlanCapDelete (DeleteView):
    model = PlanDeCapacitacion
    template_name = 'plan_cap_delete.html'
    success_url = reverse_lazy ("plan_cap")


#-------------#
#Competencias
#-------------#    
# Listar
class CompetenciasList (ListView):
    model = Competencia
    template_name = 'Competencias.html'
#-------------#
#PerfilRequer
#-------------#    
# Listar
class PerfilRequerList (ListView):
    model = PerfilRequerimiento
    template_name = 'PerfilRequer.html'

#Registrar
class PerfilRequerCreate (CreateView):
    model = PerfilRequerimiento
    form_class = PerfilRequerimientoForm
    second_form_class = PerfilForm
    thir_form_class = RequerimientoForm
    template_name = "PerfilRequer_Form.html"
    success_url = reverse_lazy ("PerfilRequer")

    def get_context_data(self, **kwargs):
        context = super (PerfilRequerCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        if 'form3' not in context:
            context['form3'] = self.thir_form_class(self.request.GET)
        return context

    def post (self, request, *args, **kargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        form3 = self.thir_form_class(request.POST)
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            R = form.save(commit=False)
            R.perfil = form2.save()
            R.requerimiento =form3.save()
            R.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form,form2=form2,form3=form3))

# Modificar
class PerfilRequerUpdate (UpdateView):
    model = PerfilRequerimiento
    second_model = Perfil
    thir_model = Requerimiento
    template_name = "PerfilRequer_Form.html"
    form_class = PerfilRequerimientoForm
    second_form_class = PerfilForm
    thir_form_class = RequerimientoForm
    success_url = reverse_lazy ("PerfilRequer")

    def get_context_data (self, **kwargs):
        context = super(PerfilRequerUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        PerfilRequerimiento = self.model.objects.get(id=pk)
        Perfil = self.second_model.objects.get(id=PerfilRequerimiento.perfil_id)
        Requerimiento = self.thir_model.objects.get(id=PerfilRequerimiento.requerimiento_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance = PerfilRequerimiento.perfil)
        if 'form3' not in context:
            context['form3'] = self.thir_form_class(instance = PerfilRequerimiento.requerimiento)
        context ['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_PerfilRequerimiento = kwargs['pk']
        PerfilRequerimiento = self.model.objects.get(id=id_PerfilRequerimiento)
        Perfil = self.second_model.objects.get(id=PerfilRequerimiento.perfil_id)
        Requerimiento = self.thir_model.objects.get(id=PerfilRequerimiento.requerimiento_id)
        form = self.form_class(request.POST, instance = PerfilRequerimiento)
        form2 = self.second_form_class(request.POST, instance = Perfil)
        form3 = self.thir_form_class(request.POST, instance = Requerimiento)
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            form.save()
            form2.save()
            form3.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())

# Eliminar

class PerfilRequerDelete (DeleteView):
    model = PerfilRequerimiento
    template_name = "PerfilRequer_delete.html"
    success_url = reverse_lazy ("PerfilRequer")
