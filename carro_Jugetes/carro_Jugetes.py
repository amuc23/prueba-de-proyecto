class CARRO_jugetes:
    def __init__(self, request):
        if request.user.is_authenticated:
            self.request = request
            self.session = request.session
            carro_jugetes = self.session.get("CARRO_jugetes")
            self.CARRO_jugetes = carro_jugetes if carro_jugetes else {}


    def agregar_jugetes(self, jugete):
        jugeteid = str(jugete.idjugete)
        if jugeteid not in self.CARRO_jugetes:
            self.CARRO_jugetes[jugeteid] = {
                "jugeteid": jugete.idjugete,
                "nombre": jugete.nombre,
                "precio": str(jugete.precio),
                "Stock": 1,  
                "imagen": jugete.imagen.url,
            }
        else:
            self.CARRO_jugetes[jugeteid]["Stock"] += 1
        self.guardar_carro_jugetes()
        

    def restar_jugetes(self, jugete):
        jugeteid = str(jugete.idjugete)
        if jugeteid in self.CARRO_jugetes:
            if self.CARRO_jugetes[jugeteid]["Stock"] > 1:
                self.CARRO_jugetes[jugeteid]["Stock"] -= 1
            else:
                self.eliminar_jugetes(jugete)
            self.guardar_carro_jugetes()


    def eliminar_jugetes(self, jugete):
        jugeteid = str(jugete.idjugete)
        if jugeteid in self.CARRO_jugetes:
            del self.CARRO_jugetes[jugeteid]
            self.guardar_carro_jugetes()


    def limpiar_carro_jugetes(self):
        self.session["CARRO_jugetes"] = {}
        self.session.modified = True


    def guardar_carro_jugetes(self):
        self.session["CARRO_jugetes"] = self.CARRO_jugetes
        self.session.modified = True
