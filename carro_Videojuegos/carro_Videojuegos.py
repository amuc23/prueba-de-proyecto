class CARRO_videojuegos:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro_videojuegos = self.session.get("CARRO_videojuegos")
        self.CARRO_videojuegos = carro_videojuegos if carro_videojuegos else {}

    def agregar_videojuegos(self, videojuego):
        videojuego_id = str(videojuego.id)
        if videojuego_id not in self.CARRO_videojuegos:
            self.CARRO_videojuegos[videojuego_id] = {
                "videojuego_id": videojuego.id,
                "nombre": videojuego.nombre,
                "precio": str(videojuego.precio),
                "Stock": 1,  # Asegúrate de que 'Stock' sea consistente
                "imagen": videojuego.imagen.url,
            }
        else:
            self.CARRO_videojuegos[videojuego_id]["Stock"] += 1

        self.guardar_carro_videojuegos()

    def restar_videojuegos(self, videojuego):
        videojuego_id = str(videojuego.id)
        if videojuego_id in self.CARRO_videojuegos:
            if self.CARRO_videojuegos[videojuego_id]["Stock"] > 1:
                self.CARRO_videojuegos[videojuego_id]["Stock"] -= 1
            else:
                self.eliminar_videojuegos(videojuego)
            self.guardar_carro_videojuegos()

    def eliminar_videojuegos(self, videojuego):
        videojuego_id = str(videojuego.id)
        if videojuego_id in self.CARRO_videojuegos:
            del self.CARRO_videojuegos[videojuego_id]
            self.guardar_carro_videojuegos()

    def limpiar_carro_videojuegos(self):
        self.session["CARRO_videojuegos"] = {}
        self.session.modified = True

    def guardar_carro_videojuegos(self):
        self.session["CARRO_videojuegos"] = self.CARRO_videojuegos
        self.session.modified = True

        

        
        
############################################################


        