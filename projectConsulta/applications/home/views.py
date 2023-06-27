from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView
# Create your views here.



class Inicio(TemplateView):
    template_name = "app1/inicio.html"

class Inicio2(TemplateView):
    template_name = "home/home.html"

