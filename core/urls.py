from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('Carreras/',views.Carrera, name = 'carreras'),
    path('Docentes/',views.docente, name = 'docentes'),
] 