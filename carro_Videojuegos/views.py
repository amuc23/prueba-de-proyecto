from django.shortcuts import render

from .carro_Videojuegos import CARRO_videojuegos 

from megagames.models import Videojuego

from django.shortcuts import redirect

 

# Create your views here.

def agregar_videojuego(request, videojuego_id):
    # Crear una instancia del carro de la compra
    carroV = CARRO_videojuegos(request)
    # Obtener el objeto Videojuego por su id
    productoJ = Videojuego.objects.get(id=videojuego_id)
    # Agregar el videojuego al carro (dependiendo de cómo esté definido el método agregar_videojuegos)
    carroV.agregar_videojuegos(productoJ)

    # Redirigir a la vista 'juego' (reemplaza 'juego' con el nombre de tu vista destino)
    return redirect("juego")



# Función para eliminar un videojuego del carro
def eliminar_videojuego(request, videojuego_id):
    carroV = CARRO_videojuegos(request)
    productoJ = Videojuego.objects.get(id=videojuego_id)
    carroV.eliminar_videojuegos(productoJ)
    return redirect("juego")

# Función para restar un videojuego del carro
def restar_videojuego(request, videojuego_id):
    carroV = CARRO_videojuegos(request)
    productoJ = Videojuego.objects.get(id=videojuego_id)
    carroV.restar_videojuegos(productoJ)
    return redirect("juego")

# Función para limpiar el carro
def limpiar_carro_videojuegos(request):
    carroV = CARRO_videojuegos(request)
    carroV.limpiar_carro_videojuegos()
    return redirect("carrito")



####################################

##apartado exclusiv carroto
#apartado exclusivo para sumar y restar desde el carrito
# Función para agregar videojuegos al carrito
def agregar_videojuego2(request, videojuego_id):
    carroV = CARRO_videojuegos(request)
    productoJ = Videojuego.objects.get(id=videojuego_id)
    carroV.agregar_videojuegos(productoJ)
    return redirect("carrito")

# Función para eliminar videojuegos del carrito
def eliminar_videojuego2(request, videojuego_id):
    carroV = CARRO_videojuegos(request)
    productoJ = Videojuego.objects.get(id=videojuego_id)
    carroV.eliminar_videojuegos(productoJ)
    return redirect("carrito")

# Función para restar videojuegos del carrito
def restar_videojuego2(request, videojuego_id):
    carroV = CARRO_videojuegos(request)
    productoJ = Videojuego.objects.get(id=videojuego_id)
    carroV.restar_videojuegos(productoJ)
    return redirect("carrito")

# Función para limpiar el carrito de videojuegos
def limpiar_carro_videojuegos2(request):
    carroV = CARRO_videojuegos(request)
    carroV.limpiar_carro_videojuegos()
    return redirect("carrito")




