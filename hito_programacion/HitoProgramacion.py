import random
import pandas as pd
from datetime import date   #Importamos date del modulo datetime para hacer una fecha aleatoria para el envío.

Finicio = date.today()  #Ponemos que la fecha de inicio sea la de hoy.
Ffinal =  date(2022, 12, 30)    #Ponemos una fecha máxima.

fechaAleatoria = Finicio + (Ffinal - Finicio) * random.random() #Nos da una fecha aleatoria entre esas dos.

productos=["manzanas","peras","melon","fresas","platanos"]  #Creamos tres listas con el nombre del producto, el precio y el stock.
precio=[0.20,0.15,3,0.10,0.25]
stock=[540,245,120,765,400]


class Cliente:  #Creamos la clase cliente para el registro del cliente. 
    def preguntaRegistro(self): #Creamos una función para que nos pregunte si el usuario está registrado o no.
        pregRegistro=input("¿Está usted registrado? (si/no): ") #Elegimos si o no.
        if pregRegistro.lower()=="si":  #Si la respuesta es si, entonces nos hacemos "Login".
            self.nombreCliente=input("Ingrese el nombre de usuario: ")  #Ponemos el nombre.
            self.contraseñaCliente=input("Ingrese la contraseña: ") #Ponemos la contraseña.
            print() #Todos los print() son saltos de línea.
            print("Ha iniciado sesión satisfactoriamente.")
            print()
            print("------------------------------------------------------------------------------") #Esto es un separador, es unicamente decorativo.
            print()
        elif pregRegistro.lower()=="no":    #Si la respuesta es no
            self.nombreCliente=input("Ingrese el nombre de usuario: ")  #ingresamos el usuario, correo, contraseña, telefono y dni para registrarnos.
            self.correoCliente=input("Ingrese el correo electrónico: ")
            self.contraseñaCliente=input("Ingrese una contraseña: ")
            self.telefono=input("Ingrese su número de teléfono: ")
            self.dni=input("Ingrese el DNI: ")
            print()
            print("------------------------------------------------------------------------------")
            print()
            
            while "@" not in self.correoCliente:    #Mientras que no haya una @ en el correo nos va a decir que ha habido un error.
                print("Hay un error en el registro, pruebe de nuevo.")
                print()
                print("------------------------------------------------------------------------------")
                print()
                correoClienteNuevo=input("Ingrese el correo electrónico de nuevo: ")    #Nos pide de nuevo el correo.
                if correoClienteNuevo.__contains__("@"):    #Si en el nuevo correo hay @
                    datos=[self.nombreCliente,correoClienteNuevo,self.contraseñaCliente,self.telefono,self.dni] #Creamos una lista.
                    print("El usuario se ha registrado correctamente.") #Nos dice que nos hemos registrado correctamente.
                    print()
                    df1=pd.DataFrame(datos, index=["Usuario","e-mail","contraseña","Tlf","DNI"])    #Nos muestra los datos del registro.
                    df1.set_axis(["Datos"], axis=1) #Nos pone como título "Datos".
                    print("Datos: \n%s" % df1)
                    print()
                    print("------------------------------------------------------------------------------")
                    print()
                    break
            if self.correoCliente.__contains__("@"):    #Si en el correo original hay una @ pasa lo mismo que en apartado anterior.
                datos=[self.nombreCliente,self.correoCliente,self.contraseñaCliente,self.telefono,self.dni]
                print("El usuario se ha registrado correctamente.")
                print()
                df1=pd.DataFrame(datos, index=["Usuario","e-mail","contraseña","Tlf","DNI"])
                df1.set_axis(["Datos"], axis=1)
                print("Datos: \n%s" % df1)
                print()
                print("------------------------------------------------------------------------------")
                print()
            
                    
        
cliente1=Cliente()  #Instanciamos a la clase Cliente.
cliente1.preguntaRegistro() #Llamamos al método "preguntaRegistro()"

print("Disponemos de los siguientes productos: ")   #Con las listas del principio hacemos que nos muestre los productos, stock y precio de cada uno en forma de tabla gracias a pandas.
print()
dict={"NombreProducto": productos, "Precio": precio, "Stock": stock}    #Hacemos un diccionario llamando a las listas creadas al principio del código en forma de columnas.
df2=pd.DataFrame(dict, index=["Producto 1","Producto 2","Producto 3","Producto 4","Producto 5"])    #Hacemos una variable llamada df y a continuación hacemos el esquema llamando al módulo pandas como pd y poniendo DataFrame.
                                                                                                    #DataFrame sirve para crear una estructura de datos formada a partir de filas y columnas.
print(df2)  #Imprimimos el esquema.
print()
print("------------------------------------------------------------------------------")
print()

class Producto(Cliente):    #Creamos la clase Producto que hereda de Cliente.
    def __init__(self) -> None: #Creamos un constructor.
        self.nombreProducto=input("Ingrese el nombre del producto deseado: ")   #Ahora hacemos que nos pida el nombre del producto y el número de prodcutos.
        self.cantidadProducto=input("Ingrese el número de productos: ")

    def productos(self):    #Creamos el método productos para el cálculo de los productos deseados.
        j=len(productos)    #La variable j sirve para que se quede guardado el número de elementos de la lista productos.
        i=0                 #Creamos un totalizador.
        while i < j:    #Hacemos un bucle en el cual mientras i sea menor que j hará una serie de procesos.
            if productos[i]==self.nombreProducto:    #Creamos una condicional para que haga una acción si el nombre del producto está en la lista.
                if int(self.cantidadProducto) > stock[i]:   #Hacemos otra condicional en la que si la cantidad de producto deseada es mayor que en la lista stock nos diga que no es posible (convertimos primero la cantidad de productos a int ya que era un str originalmente).
                    print("No es posible, el stock máximo es "+str(stock[i]), ", vuelva a iniciar el proceso.")
                else:   #Si la cantidad pedida es menor que el stock, entonces continuamos el proceso.
                    comprobar=input(f"En su carrito tiene {self.cantidadProducto} {productos[i]}, ¿está seguro de su compra?: ")    #Hacemos un carrito de la compra que nos
                    print()                                                                                                         #pregunta si estamos seguros.
                    if comprobar.lower()=="si": #Hacemos una condicional en la que si decimos que sí se inicia el ultimo proceso, el cálculo.
                        self.paisCliente=input("Ingrese el país desde el que hace el pedido: ") #Hacemos que nos pida el país desde el que pedimos el producto.
                        precioSinIVA=float(self.cantidadProducto)*precio[i] #Hacemos la variable precioSinIVA, convertimos a float la cantidadProducto y lo multiplicamos por el respectivo lugar en la lista de los precios.
                        stockRestante=stock[i]-int(self.cantidadProducto)   #Hacemos la resta para ver el stock restante.
                        print(f"El precio sin IVA es {precioSinIVA}€, quedan {stockRestante} unidades en stock.")   #Nos imprime el resultado de ambos procesos.
                        if self.paisCliente=="España":  #Última condicional, aquí entra en juego el self.paisCliente.
                            precioConIVA=precioSinIVA*1.21  #Si el país es España entonces se aplicará el impuesto correspondiente.
                            print(f"El total con el IVA es {precioConIVA:.2f}€.")   #Hacemos :.2f para que el precio total nos salga solamente con dos decimales.
                            print()
                            print(f"Se le ha mandado un PDF al correo electrónico.")    #Nos imprime que nos ha mandado un correo.
                            print(f"Se le ha mandado un SMS al número de teléfono con el cual puede ver el seguimiento.")   #Nos imprime que nos ha mandado un SMS para ver el seguimiento.
                            print(f"La fecha de envío es {fechaAleatoria}") #Nos pone la fecha de envío aleatoria que hemos puesto declarado arriba.
                        elif self.paisCliente!="España":    #Si el país no es España
                            precioConIVA=precioSinIVA*(random.uniform(1,2)) #entonces cogerá un número aleatorio entre 1 y 2 para el IVA de un país cualquiera.
                            print(f"El total con el IVA añadido de su respectivo país es {precioConIVA:.2f}€.") #(Imprime lo mismo que en el caso de que el país fuese España)
                            print()  
                            print(f"Se le ha mandado un PDF al correo electrónico.")
                            print(f"Se le ha mandado un SMS al número de teléfono con el cual puede ver el seguimiento.")
                            print(f"La fecha de envío es {fechaAleatoria}")
                    else:
                        print("Vuelva a iniciar el proceso para seleccionar los productos deseados.")   #Si no estamos seguros de la compra que hemos hecho entonces nos dirá
                                                                                                        #que iniciemos el proceso de nuevo.
            i=i+1   #Creamos una suma dentro del bucle.

producto1=Producto()    #Instanciamos a la clase producto.
producto1.productos()   #Llamamos al método.