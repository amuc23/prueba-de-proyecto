#creacion de variables globales

#acumulador del preico final (repetir para consola y videojuegos)
#al repetir sumar a la misma variable

# carro_Videojuegos/context_processor.py



def valor_final_carrito(request):
    precio_total = 0

    if request.user.is_authenticated:
        # Verifica si el carrito de videojuegos está presente y no está vacío
        if "CARRO_videojuegos" in request.session and request.session["CARRO_videojuegos"]:
            carritoJ = request.session["CARRO_videojuegos"]
            for key, value in carritoJ.items():
                precio_total += int(value["precio"]) * int(value["Stock"])

        # Verifica si el carrito de juguetes está presente y no está vacío
        if "CARRO_jugetes" in request.session and request.session["CARRO_jugetes"]:
            carritoJGT = request.session["CARRO_jugetes"]
            for key, value in carritoJGT.items():
                precio_total += int(value["precio"]) * int(value["Stock"])

        # Verifica si el carrito de consolas está presente y no está vacío
        if "CARRO_consolas" in request.session and request.session["CARRO_consolas"]:
            carritoC = request.session["CARRO_consolas"]
            for key, value in carritoC.items():
                precio_total += int(value["precio"]) * int(value["Stock"])

    return {'precio_total': precio_total}

