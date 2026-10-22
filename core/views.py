from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'core/home.html')

def Carrera(request):
    list_carrera =['Ingenieria en Sistemas Computacionales','Ingenieria Industrial','Ingenieria Mecatronica',
                   'Ingenieria en Energias Renovables','Ingenieria en Gestion Empresarial','Ingenieria en Logistica y Transporte'
                   ,'Ingenieria en Tecnologia de la Informacion y Comunicacion']
    
    return render(request,"core/Carreras.html",{'carreras' : list_carrera})

def docente(request):
    return render(request,"core/Docentes.html")