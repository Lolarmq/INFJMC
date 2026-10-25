from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def carreras(request):
    lista_Carreras = [
        'Ingenieria Informatica',
        'Ingenieria Civil',
        'Ingenieria Comercial',
        'Ingenieria en Sistemas Computacionales',
        'Ingenieria Industrial',
        'Ingenieria Mecatronica',
        'Ingenieria en Energias Renovables',
        'Ingenieria en Gestion Empresarial',
        'Ingenieria en Logistica y Transporte',
        'Ingenieria en Tecnologia de la Informacion y Comunicacion'
    ]
    return render(request, 'core/carreras.html', {'carreras': lista_Carreras})

def docentes(request):
    lista_docentes = [
        'Pamela Gatica','Dr. Juan Peres'
        'Gabriel Jara', 'Dra. Maria Lopez',
        'Rodrigo Pinochet', 'Dra Laura Gomez',
        'Ing. Carlos Sanchez', 'Ing. Pedro Martinez'
    ]
    return render(request, 'core/docentes.html',{'docentes':lista_docentes})

def home2(request):
    return render(request, 'core/home2.html')

def carreras2(request):
    lista_Carreras = [
        'Ingenieria Informatica',
        'Ingenieria Civil',
        'Ingenieria Comercial',
        'Ingenieria en Sistemas Computacionales',
        'Ingenieria Industrial',
        'Ingenieria Mecatronica',
        'Ingenieria en Energias Renovables',
        'Ingenieria en Gestion Empresarial',
        'Ingenieria en Logistica y Transporte',
        'Ingenieria en Tecnologia de la Informacion y Comunicacion'
    ]
    return render(request, 'core/carreras2.html', {'carreras': lista_Carreras})

def docentes2(request):
    lista_docentes = [
        'Pamela Gatica','Dr. Juan Peres',
        'Gabriel Jara', 'Dra. Maria Lopez',
        'Rodrigo Pinochet', 'Dra Laura Gomez',
        'Ing. Carlos Sanchez', 'Ing. Pedro Martinez'
    ]
    return render(request, 'core/docentes2.html',{'docentes':lista_docentes})