from django.shortcuts import render
from .models import Proyecto, Experiencia, Habilidad, Lenguaje, Social, Trabajo, Usuario

def home(request):
    return render(request, "pages/home.html", {})

# views.py
def portfolio_view(request):
    proyectos = Proyecto.objects.all()
    experiencias = Experiencia.objects.all()
    habilidades = Habilidad.objects.all()
    lenguajes = Lenguaje.objects.all()
    sociales = Social.objects.all()
    trabajos = Trabajo.objects.all()
    usuarios = Usuario.objects.all()

    context = {
        'proyectos': proyectos,
        'experiencias': experiencias,
        'habilidades': habilidades,
        'lenguajes': lenguajes,
        'sociales': sociales,
        'trabajos': trabajos,
        'usuarios': usuarios,
    }
    
    return render(request, 'pages/portfolio.html', context)
