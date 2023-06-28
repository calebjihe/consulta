from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView
# Create your views here.
from .models import Municipio


class Inicio(TemplateView):
    template_name = "app1/inicio.html"

class Inicio2(TemplateView):
    template_name = "home/home.html"

class MunicipiosConsListView(ListView):
    model = Municipio
    context_object_name= 'municipios'
    template_name = "home/home.html"


class PresidenteDetailView(DetailView):
    model = Municipio
    template_name = "home/inicio.html"
