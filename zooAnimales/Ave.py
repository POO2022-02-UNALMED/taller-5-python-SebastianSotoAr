from zooAnimales import Animal

class Ave(Animal):
    halcones = 0
    aguilas = 0
    listado = []

    def __init__(self, nombre = "", edad = 0, habitat = 0, genero = "", colorPlumas = ""):
        super.__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave.listado.append(self)

    def cantidadAves(self):
        return len(Ave.listado)

    def movimiento(self):
        return "volar"

    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        halcon = Ave(nombre, edad, "montañas", genero, "cafe glorioso")
        cls.halcones += 1
        return halcon

    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        aguila = Ave(nombre, edad, "montañas", genero, "blanco y amarillo")
        cls.aguilas += 1
        return aguila

    def getColorPlumas(self):
        return self._colorPlumas

    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas