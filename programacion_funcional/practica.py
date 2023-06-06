#Ejercicio1
#creas una clase en python para almacenar Productos
#los atributos son nombre, color, unidades, precio
#si quieres utiliza un constructor
#crea un método que permita mostrar el info del producto: nombre, stock, unidades
#da de alta tres prodcutos a tu gusto.

from operator import add
from functools import reduce


class Productos:
    def __init__(self,nombre,unidades,precio) -> None:
        self.nombre=nombre
        self.unidades=unidades
        self.precio=precio
    def detalles(self):
        print(f"Nombre: {self.nombre}   Unidades: {self.unidades}   Precio: {self.precio}")
    def getUnidades(self):
        return self.unidades
    def getPrecio(self):
        return self.precio

producto1=Productos("Camisetas",4,10)
producto2=Productos("Pantalones",9,15.95)
producto3=Productos("Gorras",2,5.95)
producto1.detalles()
producto2.detalles()
producto3.detalles()

#Ejercicio 2
#Creas 5 productos - list
#1. total de unidades
#2. total de importe  unidad*precio
#3. total de factura con 21% IVA incluido

productos=[producto1,producto2,producto3]

#1. total de unidades
totalUnidades=map(lambda p:p.getUnidades(),productos)
#sumaTotalUnidades=reduce(add,list(totalUnidades))
sumaTotalUnidades=reduce(add,list(map(lambda p:p.getUnidades(),productos)))
print(list(totalUnidades))
print(f"Las unidades totales son: {sumaTotalUnidades}")

#2. total de importe  unidad*precio
totalPrecio=map(lambda p:p.getPrecio(),productos)
#sumaTotalUnidades=reduce(add,list(totalUnidades))
sumaTotalPrecio=reduce(add,list(map(lambda p:p.getPrecio(),productos)))
print(list(totalPrecio))
print(f"El precio total es {sumaTotalPrecio*sumaTotalUnidades}")

#3. total de factura con 21% IVA incluido
print(f"El total de la factura es {sumaTotalPrecio*sumaTotalUnidades*1.21}")

