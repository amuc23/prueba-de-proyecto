#creacion de variables globales

#acumulador del preico final (repetir para consola y videojuegos)
#al repetir sumar a la misma variable

# carro_Videojuegos/context_processor.py

def valor_final_carrito(request):
    precio_total = 0
    if request.user.is_authenticated:
        if "CARRO_jugetes" in request.session:
            carrito = request.session["CARRO_jugetes"]
            for key, value in carrito.items():
                precio_total += int(value["precio"]) * int(value["Stock"])
    return {'precio_total': precio_total}