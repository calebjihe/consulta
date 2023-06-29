from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
# Create your views here.
from .models import Municipio


class MunicipiosListView(ListView):
    model = Municipio
    context_object_name= 'municipios'
    template_name = "home/home.html"

class PresidenteDetailView(ListView):
    model = Municipio
    context_object_name= 'municipios'
    template_name = "home/home.html"
    def get_queryset(self):
        #self.request.GET.get("")
        pkv=self.request.GET.get("pk")
        cvb=self.kwargs.get('pk')
        print("<<<<<<<<<<<<<<<<<<<<<<")
        print(str(cvb))
        print(type(pkv))
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>")
        ser=Municipio.objects.get(id=115)
        print("**********************")
        print(ser.munlocales.all())
        print("***********+++++++++++***********")
        print(ser.munfederales.all())
        
        return ser.munlocales.all()
    
    

class DetallesDetailView(DetailView):
    print("mmmmmmmmmmmmmmmmm")
    model = Municipio
    #context_object_name= 'mun'
    template_name = "home/home.html"
    
    
    
    def get_context_data(self, **kwargs):
        context = super(DetallesDetailView, self).get_context_data(**kwargs)
        #context['something'] =Municipio.objects.filter(pk=self.kwargs.get('pk'))
        cvb=self.kwargs.get('pk')
        ser=Municipio.objects.get(id=cvb)
        print("++++22")
        print(ser.munlocales.all())
        
        context['something']=ser.munlocales.all()
        print("lllllllllllllllllll")
        print(context['something'])
        return context
    
    


class ListaMunicioListView(ListView):
    context_object_name= 'mun'
    template_name = "home/inicio.html"

    def get_queryset(self):
        
        idkey = self.kwargs['idmun']
        print("kkkkkkkkkkkk")
        print(type(idkey))
        lista = Municipio.objects.get(id=int(idkey))
        locales=lista.munlocales.all()
        federales =lista.munfederales.all()
        answers_list = list(locales)
        answers_list1 = list(federales)
        ll= answers_list+answers_list1

        #ll=locales+federales
        print("type(locales)  ",type(locales))
        print("type(federales)  ",type(federales))
        #return lista.munlocales.all()
        return ll

    
    
    

    


    
