from django import forms
from .models import Videojuego

class VideojuegoForm(forms.ModelForm):
    class Meta:
        model = Videojuego
        # Seleccionamos los 3 campos a usar en el formulario
        fields = ['nombre', 'duracion_horas', 'ao_lanzamiento'] 
        
        # Etiquetas (labels) personalizadas para el usuario
        labels = {
            'nombre': 'Título del Videojuego',
            'duracion_horas': 'Duración (en horas)',
            'ao_lanzamiento': 'Año de Lanzamiento',
        }
        
        # Widgets para aplicar estilos de Bootstrap a los campos (opcional pero recomendado)
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'duracion_horas': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'ao_lanzamiento': forms.NumberInput(attrs={'class': 'form-control'}),
        }