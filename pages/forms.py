from django import forms
from .models import Proyecto, Experiencia, Habilidad, Lenguaje, Social, Trabajo, Usuario



class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion']

class ExperienciaForm(forms.ModelForm):
    class Meta:
        model = Experiencia
        fields = ['nombre', 'listProyecto']

class HabilidadForm(forms.ModelForm):
    class Meta:
        model = Habilidad
        fields = ['nombre', 'descripcion']

class LenguajeForm(forms.ModelForm):
    class Meta:
        model = Lenguaje
        fields = ['nombre', 'expirencia']

class SocialForm(forms.ModelForm):
    class Meta:
        model = Social
        fields = ['nombre', 'url']

class TrabajoForm(forms.ModelForm):
    class Meta:
        model = Trabajo
        fields = ['nombre', 'descripcion', 'fechaIni', 'fechaFin']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nombre', 'descripcion', 'nivel', 'imagen',
            'listHabilidad', 'listaLenguaje', 'listaTrabajo',
            'listaSocial', 'listaProyecto', 'listaExperiencia'
        ]

