# videojuegos/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Videojuego
from .forms import VideojuegoForm

# --- Lógica CRUD ---

# READ: Mostrar lista de videojuegos [29:45]
def index(request):
    videojuegos = Videojuego.objects.all()
    context = {'videojuegos': videojuegos}
    return render(request, 'videojuegos/index.html', context)

# CREATE: Añadir nuevo videojuego [01:18:44]
def add(request):
    if request.method == 'POST':
        form = VideojuegoForm(request.POST)
        if form.is_valid():
            form.save()
            # Muestra un mensaje de éxito y un formulario nuevo
            return render(request, 'videojuegos/add.html', {'form': VideojuegoForm(), 'success': True})
    else:
        # Petición GET, muestra el formulario vacío
        form = VideojuegoForm()
    
    return render(request, 'videojuegos/add.html', {'form': form})

# UPDATE: Editar un videojuego [01:39:23]
def edit(request, pk):
    # Recupera el objeto o devuelve error 404
    videojuego = get_object_or_404(Videojuego, pk=pk)
    
    if request.method == 'POST':
        # Instancia el formulario con los datos POST Y el objeto existente
        form = VideojuegoForm(request.POST, instance=videojuego)
        if form.is_valid():
            form.save()
            # Redirige a la lista principal después de actualizar
            return redirect(reverse('index')) 
    else:
        # Petición GET, muestra el formulario pre-llenado con la instancia
        form = VideojuegoForm(instance=videojuego)
    
    # 'videojuego' se pasa para poder mostrar el nombre en el encabezado
    return render(request, 'videojuegos/edit.html', {'form': form, 'videojuego': videojuego})

# DELETE: Eliminar un videojuego [01:47:09]
def delete(request, pk):
    videojuego = get_object_or_404(Videojuego, pk=pk)
    
    if request.method == 'POST':
        videojuego.delete()
        # Redirige a la lista principal después de eliminar
        return redirect(reverse('index'))
    
    # En este caso, redirigimos si no es POST, ya que la confirmación se hace en el index.html
    return redirect(reverse('index'))