from django.shortcuts import render, redirect
from django.views.generic import CreateView,DeleteView,ListView,UpdateView
from django.urls import reverse_lazy
from .forms import PersonaForm, CiudadForm,TipoDocumentoForm
from .models import Persona, Ciudad, TipoDocumento

class PersonaList(ListView):
    model = Persona
    template_name = 'index.html'

    def get_queryset(self):
        return self.model.objects.all()

class PersonaCreate(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'crear_persona.html'
    success_url = reverse_lazy('index')

class PersonaUpdate(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'crear_persona.html'
    success_url = reverse_lazy('index')

class PersonaDelete(DeleteView):
    model = Persona
    template_name = 'verificacion.html'
    success_url = reverse_lazy('index')

#--------------------------------------------------------------------------------------------------------------------------------

class CiudadList(ListView):
    model = Ciudad
    template_name = 'index.html'

    def get_queryset(self):
        return self.model.objects.all()

class CiudadCreate(CreateView):
    model = Ciudad
    form_class = CiudadForm
    template_name = 'crear_ciudad.html'
    success_url = reverse_lazy('index')

class CiudadUpdate(UpdateView):
    model = Ciudad
    form_class = CiudadForm
    template_name = 'crear_ciudad.html'
    success_url = reverse_lazy('index')

class CiudadDelete(DeleteView):
    model = Ciudad
    template_name = 'verificacion.html'
    success_url = reverse_lazy('index')

#--------------------------------------------------------------------------------------------------------------------------------

class TipoDocumentoList(ListView):
    model = TipoDocumento
    template_name = 'index.html'

    def get_queryset(self):
        return self.model.objects.all()

class TipoDocumentoCreate(CreateView):
    model = TipoDocumento
    form_class = TipoDocumentoForm
    template_name = 'crear_tipodocumento.html'
    success_url = reverse_lazy('index')

class TipoDocumentoUpdate(UpdateView):
    model = TipoDocumento
    form_class = TipoDocumentoForm
    template_name = 'crear_tipodocumento.html'
    success_url = reverse_lazy('index')

class TipoDocumentoDelete(DeleteView):
    model = TipoDocumento
    template_name = 'verificacion.html'
    success_url = reverse_lazy('index')