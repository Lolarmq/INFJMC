from django.shortcuts import render

# Create your views here.
def home(request):
    return render("Bienvenido al Area de Informatica")

def Carrera(request):
    return render("Pagina de Carreras")

def docente(rerquest):
    return render("Pagina de Docentes")
