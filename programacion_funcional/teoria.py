#Python con programación funcional.
#Características propias del paradigma declarativo.
#no vamos a utilizar condicional ni bucles como estructuras.
#utilizaremos funciones: filter, map, reduce






#función map https://ellibrodepython.com/programacion-funcional-python 
#tenemos un listado de ventas y quieres calcular el total de factura con iva incluido (21%)


from calendar import isleap
from functools import reduce
from operator import add
import statistics

ventas=[1000,1500,2100,1950.25]
totalFactura=[] #Declarar una variable de tipo lista para guardar resultados

def calcularTotal(x):
    return x*1.21

#imperativo. ciclo for
for venta in ventas:
    totalFactura.append(venta*1.21)

print(totalFactura) #muestra al finalizar

#declarativo. función map
totalFactura=map(calcularTotal,ventas)  #map tiene un ciclo bucle dentro
print(f"Programación funcional: {list(totalFactura)}")  #función list para convertir map a lista

#list() #Función para convertir de map a lista
#list [] (dictionary{},sets{}) #Son colecciones

#--------------------------------------------------

#Práctica
#tienes una lista de ciudades
#mostrar las ciudades en mayúsculas

ciudades=["Madrid","Tokio","Kioto","Seúl","Busan"]

#Imperativo

ciudadesM=[]
for ciudad in ciudades:
    ciudadesM.append(ciudad.upper())

print(ciudadesM)

#Funcional (map solo)
def mayusculas(x):
    return x.upper()

ciudadesM=map(mayusculas,ciudades)
print(f"Programación funcional: {list(ciudadesM)}")

#declarativo map con Lambda
ciudadesM=map(lambda x: x.upper(),ciudades)
print(list(ciudadesM))

#---------------------------------------------------------

#filter https://ellibrodepython.com/programacion-funcional-python

numeros=[10,15,12,17,5]
pares=filter(lambda n: n%2==0,numeros)
print(f"Los numeros pares son: {list(pares)}")

#---------------------------------

#Práctica de filter
#Crea una lista de años
años=[1980,1850,2014,2004,2015,2156]
#muestra los años que son bisiestos: función en python que devuelve si es o no bisiesto
#importar modulo

bisiestos=filter(lambda a:isleap(a),años)
print(f"Los años bisiestos son: {list(bisiestos)}")

#----------------------------------

#reduce https://ellibrodepython.com/programacion-funcional-python

facturacionClientes=[1500,1800,950,147.8]
sumaTotal=reduce(lambda factura,total:factura+total,facturacionClientes)
print(f"El total de facturación es {sumaTotal}")

#-----------------------------------------

#Practica reduce
#un alumno tiene las notas de 5 asignaturas
#muestra la suma total de su nota
#muestra la nota media

notasAlumno=[7,9,10,4,6]
sumaNotas=reduce(lambda notas,totalNotas:notas+totalNotas,notasAlumno)
print(f"Suma total de las notas: {sumaNotas}     Nota media: {sumaNotas/len(notasAlumno)}")

#--------------------------------------------

#Practica
#Por consola te pide un numero
#te lo sigue pidiendo hasta que pulsas 9
#cuando ya has acabado te dice:
#cuantos numeros has introducido
#su suma total
#y la media
#puedes mezclar imperativa y declarativa

#problema
#algoritmo. pasos
#pedir número
#seguir pidiendo hasta un límite
#acumular todos los números en list (no puede ser set porque se deben repetir)
#tengo la lista: declarativa: map, reduce: apra que calcule el contador, total y media


numerosPedidos=[]
while True:
    numeroPedido=int(input("Dime un número: "))
    if numeroPedido==9:
        break
    else:
        numerosPedidos.append(numeroPedido)
print(numerosPedidos)

totalPedidos=reduce(add,numerosPedidos)

print(f"La suma total de los números pedidos es {totalPedidos}")
print(f"El número total de números pedidos es {len(numerosPedidos)}")
print(f"La media de todos los números pedido es {totalPedidos/len(totalPedidos)}")


