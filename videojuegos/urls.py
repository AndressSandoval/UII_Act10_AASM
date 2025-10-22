from django.urls import path
from . import views

urlpatterns = [
    # READ: Lista todos los videojuegos (Home)
    path('', views.index, name='index'), 
    
    # CREATE: Muestra el formulario y procesa la creación
    path('add/', views.add, name='add'),
    
    # UPDATE: Muestra el formulario prellenado y procesa la actualización (usa el PK como ID)
    path('edit/<int:pk>/', views.edit, name='edit'),
    
    # DELETE: Procesa la eliminación de un registro (usa el PK como ID)
    path('delete/<int:pk>/', views.delete, name='delete'),
]