#https://ellibrodepython.com/encapsulamiento-poo
#Características de POO
#Modificadores de acceso: private, public, protected...
#ocultar atributos, métodos o clases al resto.

#protected. Únicamente se puede usar en sus clases derivadas(hijas).

class Encapsular():
    nombre="clase encapsulada"  #atributo sin nada, es público
    __ciudad="Sevilla"    #atributo private, únicamente accesible en la clase.
    def __secreto(self):  #Método de instancia privado (No accesible nada más que desde la instancia de la clase)
        print("Mensaje secreto")
    def _paraHija(self):
        print("Mensaje para hija")
        pass
class Hija(Encapsular):
    pass

encapsulamiento=Encapsular()
print(encapsulamiento.nombre)
#print(encapsulamiento.__ciudad) #No es accesible desde fuera de la clase
#encapsulamiento.__secreto()

hija=Hija()
print(hija.nombre)  #ok porque el método nombre es público
#print(hija.ciudad)  #error porq ciudad es private
#hija.secreto() #error porque secreto es private
hija._paraHija()