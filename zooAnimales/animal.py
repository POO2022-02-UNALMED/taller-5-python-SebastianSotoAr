from gestion.zona import Zona

class Animal:
    totalAnimales = 0

    def __init__(self, nombre = "", edad = 0, habitat = "", genero = ""):
        Animal.totalAnimales += 1
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None

    def movimiento(self):
        return "desplazarse"

    def toString(self):
        if (self._zona == None):
            return ("Mi nombre es "+self._nombre+", tengo una edad de "+self._edad+", habito en "+self._habitat+" y mi genero es "+self._genero)

        else:
            return ("Mi nombre es "+self._nombre+", tengo una edad de "+self._edad+", habito en "+self._habitat+" y mi genero es "+self._genero+". la zona en la que me ubico es "+self._zona.getNombre()+", en el "+self._zona.getZoo().getNombre())

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getEdad(self):
        return self._edad

    def setEdad(self, edad):
        self._edad = edad

    def getHabitat(self):
        return self._habitat

    def setHabitat(self, habitat):
        self._habitat = habitat

    def getGenero(self):
        return self._genero

    def setGenero(self, genero):
        self._genero = genero

    def getZona(self):
        return self._zona

    def setZona(self, zona):
        self._zona = zona

    @classmethod
    def totalPorTipo(cls):
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.animal import Animal
        from zooAnimales.ave import Ave
        from zooAnimales.pez import Pez
        from zooAnimales.reptil import Reptil
        return (f"Mamiferos : {Mamifero.cantidadMamiferos()}\nAves : {Ave.cantidadAves()}\nReptiles : {Reptil.cantidadReptiles()}\nPeces : {Pez.cantidadPeces()}\nAnfibios : {Anfibio.cantidadAnfibios()}")