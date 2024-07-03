

from django.shortcuts import render

from .carro_Consolas import CARRO_consolas 

from megagames.models import Consola

from django.shortcuts import redirect

# Create your views here.


def agregar_consola(request, consolaid):
    # Crear una instancia del carro de la compra
    carroVCSL = CARRO_consolas(request)
    # Obtener el objeto por su id
    productoCLS = Consola.objects.get(idconsola=consolaid)
    # Agregar al carro 
    carroVCSL.agregar_consolas(productoCLS)
    return redirect("consolas")


# Función para eliminar del carro
def eliminar_consola(request, consolaid):
    carroVCSL = CARRO_consolas(request)
    productoCLS = Consola.objects.get(idconsola=consolaid)
    carroVCSL.eliminar_consolas(productoCLS)
    return redirect("consolas")

# Función para restar  del carro
def restar_consola(request, consolaid):
    carroVCSL = CARRO_consolas(request)
    productoCLS = Consola.objects.get(idconsola=consolaid)
    carroVCSL.restar_jugetes(productoCLS)
    return redirect("consolas")

# Función para limpiar el carro
def limpiar_carro_consola(request):
    carroVCSL = CARRO_consolas(request)
    carroVCSL.limpiar_carro_consolas()
    return redirect("carrito")



####################################

##apartado exclusiv carroto
#apartado exclusivo para sumar y restar desde el carrito
# Función para agregar jugetes al carrito
def agregar_consola2(request, consolaid):
    # Crear una instancia del carro de la compra
    carroVCSL = CARRO_consolas(request)
    # Obtener el objeto por su id
    productoCLS = Consola.objects.get(idconsola=consolaid)
    # Agregar al carro 
    carroVCSL.agregar_consolas(productoCLS)
    return redirect("carrito")


# Función para eliminar del carro
def eliminar_consola2(request, consolaid):
    carroVCSL = CARRO_consolas(request)
    productoCLS = Consola.objects.get(idconsola=consolaid)
    carroVCSL.eliminar_consolas(productoCLS)
    return redirect("carrito")

# Función para restar  del carro
def restar_consola2(request, consolaid):
    carroVCSL = CARRO_consolas(request)
    productoCLS = Consola.objects.get(idconsola=consolaid)
    carroVCSL.restar_jugetes(productoCLS)
    return redirect("carrito")

# Función para limpiar el carro
def limpiar_carro_consola2(request):
    carroVCSL = CARRO_consolas(request)
    carroVCSL.limpiar_carro_consolas()
    return redirect("carrito")
