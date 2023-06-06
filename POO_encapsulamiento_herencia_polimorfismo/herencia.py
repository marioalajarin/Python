#https://ellibrodepython.com/herencia-en-python
#Característica de POO. Python la soporta.
#Sobreescritura de métodos (override): característica de la herencia.

#clase Padre, base, superclase.
class Padre:
    nombre="María Pérez"    #Atributo
    def __init__(self,nombre,ciudad) -> None:
        self.nombre=nombre
        self.ciudad=ciudad
    @staticmethod
    def saludar():     #Método de clase
        print("Estoy saludando")  

#Herencia múltple (orden de comas)
class Madre:
    unidades=15


#clase derivada, hija, subclase.
class Hija(Padre,Madre):  #Herencia
    def __init__(self, nombre, ciudad) -> None:
        self.nombre=nombre
        self.ciudad=ciudad
        super().__init__(nombre, ciudad)
    #override   (sobreescritura)
    @staticmethod
    def saludar():  #Método de clase
        print("Estoy saludando desde la hija")
    
#instanciar las clases: crea un objeto de esa clase en memoria.
hija=Hija("Marta Sánchez","Segovia") #instancia
print(hija.nombre)
hija.saludar()
print(hija.unidades)