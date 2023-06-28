from django.urls import path

from . import views
app_name="inicio"

urlpatterns = [
    path('app1/', views.Inicio.as_view()),
    path('app2/', views.Inicio2.as_view()),
    path('app3/', views.MunicipiosConsListView.as_view()),
    path('presidente/<pk>/', views.PresidenteDetailView.as_view(), name="presidente"),
]
