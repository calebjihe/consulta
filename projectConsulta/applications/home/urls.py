from django.urls import path, include

from . import views
app_name="inicio"
urlpatterns = [
    path('app1/', views.Inicio.as_view()),
    path('app2/', views.Inicio2.as_view()),
]
