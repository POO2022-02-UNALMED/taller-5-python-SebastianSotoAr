from zooAnimales.animal import Animal

class Pez(Animal):
    salmones = 0
    bacalaos = 0
    listado = []

    def __init__(self, nombre = "", edad = 0, habitat = 0, genero = "", colorEscamas = "", cantidadAletas = 0):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez.listado.append(self)

    def cantidadPez(self):
        return len(Pez.listado)

    def movimiento(self):
        return "nadar"

    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        salmon = Pez(nombre, edad, "oceano", genero, "rojo", 6)
        cls.salmones += 1
        return salmon

    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        bacalao = Pez(nombre, edad, "oceano", genero, "rojo", 6)
        cls.bacalaos += 1
        return bacalao

    def getColorEscamas(self):
        return self._colorEscamas

    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas

    def getCantidadAletas(self):
        return self._cantidadAletas

    def setCantidadAletas(self, cantidadAletas):
        self._cantidadAletas = cantidadAletas