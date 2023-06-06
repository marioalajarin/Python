#1. Crea una lista con 6 ciudades.
#Muestra las ciudades por consola. En mayúsculas y al lado el número de letras que tiene.

#Solución: lista



ciudades=["Madrid","Valencia","Almería","Ontario","Córdoba","Granada"]
for ciudad in ciudades:
    print(f"La ciudad es {ciudad.upper()} - {len(ciudad)}")

#2. Crea una colección con 5 marcas de coche. 
#Muestra el listado de ordenado en orden descendente.

#Solución: lista
coches=["seat","renault","toyota","audi","BMW"]
coches.sort()   #lista soporta orden
coches.reverse()    #orden descendente
for coche in coches:
    print(coche)

#3. Crea una colección con 5 clientes y su facturación anual en euros.
#Muestra el total de facturación y la facturación media.

#Solución: diccionario
clientes={"Iberdrola":15000,"Endesa":24000,"Steam":92000,"Enagas":18000,"Naturgy":45000}
total=0
for v in clientes.values():
    total=total+v
print(f"El total de facturación es {total}")
print(f"El promedio de facturación es {total/len(clientes)}")

#4. Por consola te pide un número hasta que pulses 0.
#Muestra la suma total de estos números.

n=1
suma=0  #totalizador
while n!=0:
   n=int(input("Dime un número:"))
   suma = suma+n
print(f"El total es {suma}")    #Se ejecuta cuando sales del bucle

    
        
#5. En una colección introduce los precios de 6 artículos. No necesitamos los nombres de los artículos.
#Muestra el precio promedio. Si es superior a 5, indica que debemos bajar el precio un 5%

articulos=[12,75,0.1,3,7,15]
total=0
for k in articulos:
    total=total+k

print(f"El precio promedio es {total/len(articulos)}")
if (total/len(articulos))>5:
    print(f"El total aplicando el descuento es {((total/len(articulos))*0.95)}")