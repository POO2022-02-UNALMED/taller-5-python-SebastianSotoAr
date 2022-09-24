class Zona:

    def __init__(self, nombre = "", zoologico = None):
        self._nombre = nombre
        self._zoologico = zoologico
        self._animales = []

    def agregarAnimales(self, animal):
        self._animales.append(animal)
        animal.setZona(self)

    def cantidadAnimales(self):
        return len(self._animales)

    def getZoo(self):
        return self._zoologico

    def setZoo(self, zoologico):
        self._zoologico = zoologico

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def setAnimales(self, animales):
        self._animales = animales

    def getAnimales(self):
        return self._animales
