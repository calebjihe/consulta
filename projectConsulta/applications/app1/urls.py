from django.urls import path

from . import views
app_name="app1"

urlpatterns = [
    
    path('fg/<pk>/', views.MunicipiosConsListView.as_view(), name="presidente"),
]
