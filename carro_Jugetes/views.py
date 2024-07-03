from django.shortcuts import render

from .carro_Jugetes import CARRO_jugetes 

from megagames.models import Jugete

from django.shortcuts import redirect

# Create your views here.


def agregar_jugete(request, jugeteid):
    # Crear una instancia del carro de la compra
    carroVJGT = CARRO_jugetes(request)
    # Obtener el objeto por su id
    productoJGT = Jugete.objects.get(idjugete=jugeteid)
    # Agregar al carro 
    carroVJGT.agregar_jugetes(productoJGT)
    return redirect("jugetes")


# Función para eliminar del carro
def eliminar_jugete(request, jugeteid):
    carroVJGT = CARRO_jugetes(request)
    productoJGT = Jugete.objects.get(idjugete=jugeteid)
    carroVJGT.eliminar_jugetes(productoJGT)
    return redirect("jugetes")

# Función para restar  del carro
def restar_jugete(request, jugeteid):
    carroVJGT = CARRO_jugetes(request)
    productoJ = Jugete.objects.get(idjugete=jugeteid)
    carroVJGT.restar_jugetes(productoJ)
    return redirect("jugetes")

# Función para limpiar el carro
def limpiar_carro_jugetes(request):
    carroVJGT = CARRO_jugetes(request)
    carroVJGT.limpiar_carro_jugetes()
    return redirect("carrito")



####################################

##apartado exclusiv carroto
#apartado exclusivo para sumar y restar desde el carrito
# Función para agregar jugetes al carrito
def agregar_jugete2(request, jugeteid):
    # Crear una instancia del carro de la compra
    carroVJGT = CARRO_jugetes(request)
    # Obtener el objeto por su id
    productoJGT = Jugete.objects.get(idjugete=jugeteid)
    # Agregar al carro 
    carroVJGT.agregar_jugetes(productoJGT)
    return redirect("carrito")


# Función para eliminar del carro
def eliminar_jugete2(request, jugeteid):
    carroVJGT = CARRO_jugetes(request)
    productoJGT = Jugete.objects.get(idjugete=jugeteid)
    carroVJGT.eliminar_jugetes(productoJGT)
    return redirect("carrito")

# Función para restar  del carro
def restar_jugete2(request, jugeteid):
    carroVJGT = CARRO_jugetes(request)
    productoJ = Jugete.objects.get(idjugete=jugeteid)
    carroVJGT.restar_jugetes(productoJ)
    return redirect("carrito")

# Función para limpiar el carro
def limpiar_carro_jugetes2(request):
    carroVJGT = CARRO_jugetes(request)
    carroVJGT.limpiar_carro_jugetes()
    return redirect("carrito")

