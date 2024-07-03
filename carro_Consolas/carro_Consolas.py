class CARRO_consolas:
    def __init__(self, request):
        if request.user.is_authenticated:
            self.request = request
            self.session = request.session
            carro_consolas = self.session.get("CARRO_consolas")
            self.CARRO_consolas = carro_consolas if carro_consolas else {}


    def agregar_consolas(self, consola):
        consolaid = str(consola.idconsola)
        if consolaid not in self.CARRO_consolas:
            self.CARRO_consolas[consolaid] = {
                "consolaid": consola.idconsola,
                "nombre": consola.nombre,
                "precio": str(consola.precio),
                "Stock": 1,  
                "imagen": consola.imagen.url,
            }
        else:
            self.CARRO_consolas[consolaid]["Stock"] += 1
        self.guardar_carro_consolas()
        

    def restar_jugetes(self, consola):
        consolaid = str(consola.idconsola)
        if consolaid in self.CARRO_consolas:
            if self.CARRO_consolas[consolaid]["Stock"] > 1:
                self.CARRO_consolas[consolaid]["Stock"] -= 1
            else:
                self.eliminar_consolas(consola)
            self.guardar_carro_consolas()


    def eliminar_consolas(self, consola):
        consolaid = str(consola.idconsola)
        if consolaid in self.CARRO_consolas:
            del self.CARRO_consolas[consolaid]
            self.guardar_carro_consolas()


    def limpiar_carro_consolas(self):
        self.session["CARRO_consolas"] = {}
        self.session.modified = True


    def guardar_carro_consolas(self):
        self.session["CARRO_consolas"] = self.CARRO_consolas
        self.session.modified = True
