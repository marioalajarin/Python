#actividad 2
#pide por consola 5 ciudades como destino
#almacena las ciudades como consideres
#No puede darse repetición y deben mostrarse ordenadas alfabéticamente
#el usuario puede añadir o eliminar ciudades
#1 puntos. Seleccionas la lista, set, tupla, dict... correcto y lo justificas
#1 punto. El programa funciona correctamente. añades y muestras los datos
#1 punto. Muestra los datos ordenados en orden ascendente y descendente
#1 punto. añade y elimina una ciudad
#1 punto. control de errores y validación

ciudades_list=["madrid","sevilla","valencia","madrid"]   #lista. Soporta ordenar (sort()). Admite repetición (no queremos eso en este ejercicio)
ciudades2_tupla=("madrid","sevilla","valencia","madrid")  #tupla. No soporta ordenar (sort())
ciudades3_dicc={"ciudad1":"madrid","ciudad2":"sevilla","ciudad3":"valencia","ciudad4":"madrid"}  #dict (diccionario). No sosporta ordenar (sort())
ciudades4_set={"madrid","sevilla","valencia","madrid"}  #set. No soporta repetición, no soporta ordenar.


#Elegimos list aunque admite repeticion

try:
    ciudades=[]
    for i in range(1,6):
        ciudad=input(f"dime una ciudad {i}: ")
        if ciudad.lower() in ciudades:
            print("Ya está. No se va a incluir")
        else:
            ciudades.append(ciudad) #añadimos una ciudad a la lista
    ciudades.sort() #ordena alfabéticamente
    print(ciudades)
    ciudades.reverse()  #ordena al revés
    print(ciudades)
    ciudades.append("coruña")   #añadimos elementos a la lista
    print(ciudades)
    ciudades.pop()  #quitamos el último elemento de la lista.
    print(ciudades)
    for ciudad in ciudades:
        print(f"La ciudad es {ciudad}")
except:
    print("algo va mal")
finally:
    print("fin del ejercicio")