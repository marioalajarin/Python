# This is a sample Python script.
import datetime
import pandas as pd
import numpy as np


# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def actividad10():
    nombre=input("Ingrese el nombre: ")
    fecha=input("Ingrese la fecha a consultar dd-mm-yyyy: ")
    print(f"Tu nombre es {nombre} y la fecha a consultar es {fecha}")
    fechadate=datetime.datetime.strptime(fecha,"%d-%m-%Y")
    diadelmes=fechadate.day
    diadelasemana=fechadate.weekday()
    print(f"El dia del mes es {diadelmes}")
    print(f"El dia de la semana es {diadelasemana}")

    #Añadir la condición

    #EnunciadosLos días NO festivos que son 5-9-14-22 toca natación
    #Los días No festivos que son 14-19-28 toca inglés.
    #Los sábados hay partido de baloncesto.

    #La aplicación pide el nombre del usuario.
    #Pide después la fecha a consultar.
    #Y la aplicación indica al usuario qué tiene asignado.

    if diadelmes in (5,9,14,22) and diadelasemana<5:
        print("Ese día toca natación")
    if diadelmes in (14,19,28) and diadelasemana<5:
        print("Ese día toca inglés")
    if diadelasemana==5:
        print("Ese día tienes partido de baloncesto")

def prueba():
    # pide la ciudad de entrega
    # si la ciudad es madrid, valencia o barcelona, el coste de envío es 5.99
    # si es otra el coste es de 7.99
    # pero a toledo hay promoción especial y el coste es 1.99

    ciudad = input("Ingrese el nombre de la ciudad: ")
    if ciudad.lower() in ("madrid", "valencia", "barcelona"):
        print(f"Al ser de {ciudad} el coste es de 5.99€")
    elif ciudad.lower() == "toledo":
        print(f"Al ser de {ciudad} el coste es de 1.99€")
    else:
        print(f"Al ser de {ciudad} el coste es de 7.99€")

def iterar():
    #pide el primer número
    #pide el segundo número
    #muestra los números que hay entre esos dos
    #si el segundo número es menor que el primero... que muestre un mensaje diciendo que no hay

    num1=int(input("Ingrese el primer número: "))
    num2=int(input("Ingrese el segundo número: "))

    if num1>num2:
        print("No hay números")
    else:
        for i in range(num1+1, num2):
            print(i)

def librerias():
    s=pd.Series([5, 9, 6, 7, 8])
    df = pd.DataFrame(np.random.randn(10, 6))
    print(s)
    print(df)






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    #actividad10()
    #prueba()
    #iterar()
    librerias()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


