from zooAnimales import Animal

class Anfibio(Animal):
    ranas = 0
    salamandras = 0
    listado = []

    def __init__(self, nombre = "", edad = 0, habitat = 0, genero = "", colorPiel = "", venenoso = False):
        super.__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio.listado.append(self)

    def cantidadAnfibios(self):
        return len(Anfibio.listado)

    def movimiento(self):
        return "saltar"

    @classmethod
    def crearRana(cls, nombre, edad, genero):
        rana = Anfibio(nombre, edad, "selva", genero, "rojo", True)
        cls.ranas += 1
        return rana

    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        salamandra = Anfibio(nombre, edad, "selva", genero, "rojo", True)
        cls.salamandras += 1
        return salamandra

    def getColorPiel(self):
        return self._colorPiel

    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel

    def isVenenoso(self):
        return self._venenoso

    def setVenenoso(self, venenoso):
        self._venenoso = venenoso