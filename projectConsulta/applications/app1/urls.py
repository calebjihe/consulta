from django.urls import path

from . import views
app_name="app1"

urlpatterns = [
    
    path('municipios/', views.MunicipiosListView.as_view(), name="municipios"),
    path('detalle/<pk>/', views.PresidenteDetailView.as_view(), name="detalle"),
    path('mun-detalle/<idmun>/', views.ListaMunicioListView.as_view(), name="detalle-mun"),
]
