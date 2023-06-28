from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
# Create your views here.
from .models import Municipio

class MunicipiosConsListView(ListView):
    model = Municipio
    context_object_name= 'municipios'
    template_name = "home/home.html"

    def get_queryset(self):
        ser=Municipio.objects.get(id=8)
        print("**********************")
        print(ser.munlocales.all())
        return ser.munlocales.all()