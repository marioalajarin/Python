import random
import pandas as pd
from datetime import date 

Finicio = date.today() 
Ffinal =  date(2022, 12, 30)    

fechaAleatoria = Finicio + (Ffinal - Finicio) * random.random() 

productos=["manzanas","peras","melon","fresas","platanos"] 
precio=[0.20,0.15,3,0.10,0.25]
stock=[540,245,120,765,400]


class Cliente:  
    def preguntaRegistro(self): 
        pregRegistro=input("¿Está usted registrado? (si/no): ") 
        if pregRegistro.lower()=="si":  
            self.nombreCliente=input("Ingrese el nombre de usuario: ")  
            self.contraseñaCliente=input("Ingrese la contraseña: ")
            print() 
            print("Ha iniciado sesión satisfactoriamente.")
            print()
            print("------------------------------------------------------------------------------") 
            print()
        elif pregRegistro.lower()=="no":    
            self.nombreCliente=input("Ingrese el nombre de usuario: ")  
            self.correoCliente=input("Ingrese el correo electrónico: ")
            self.contraseñaCliente=input("Ingrese una contraseña: ")
            self.telefono=input("Ingrese su número de teléfono: ")
            self.dni=input("Ingrese el DNI: ")
            print()
            print("------------------------------------------------------------------------------")
            print()
            
            while "@" not in self.correoCliente:   
                print("Hay un error en el registro, pruebe de nuevo.")
                print()
                print("------------------------------------------------------------------------------")
                print()
                correoClienteNuevo=input("Ingrese el correo electrónico de nuevo: ")    
                if correoClienteNuevo.__contains__("@"):    
                    datos=[self.nombreCliente,correoClienteNuevo,self.contraseñaCliente,self.telefono,self.dni]
                    print("El usuario se ha registrado correctamente.")
                    print()
                    df1=pd.DataFrame(datos, index=["Usuario","e-mail","contraseña","Tlf","DNI"])    
                    df1.set_axis(["Datos"], axis=1)
                    print("Datos: \n%s" % df1)
                    print()
                    print("------------------------------------------------------------------------------")
                    print()
                    break
            if self.correoCliente.__contains__("@"):   
                datos=[self.nombreCliente,self.correoCliente,self.contraseñaCliente,self.telefono,self.dni]
                print("El usuario se ha registrado correctamente.")
                print()
                df1=pd.DataFrame(datos, index=["Usuario","e-mail","contraseña","Tlf","DNI"])
                df1.set_axis(["Datos"], axis=1)
                print("Datos: \n%s" % df1)
                print()
                print("------------------------------------------------------------------------------")
                print()
            
                    
        
cliente1=Cliente() 
cliente1.preguntaRegistro() 

print("Disponemos de los siguientes productos: ")  
print()
dict={"NombreProducto": productos, "Precio": precio, "Stock": stock}    
df2=pd.DataFrame(dict, index=["Producto 1","Producto 2","Producto 3","Producto 4","Producto 5"])    
                                                                                                   
print(df2) 
print()
print("------------------------------------------------------------------------------")
print()

class Producto(Cliente):    
    def __init__(self) -> None:
        self.nombreProducto=input("Ingrese el nombre del producto deseado: ")
        self.cantidadProducto=input("Ingrese el número de productos: ")

    def productos(self):   
        j=len(productos)   
        i=0                
        while i < j:   
            if productos[i]==self.nombreProducto:  
                if int(self.cantidadProducto) > stock[i]:  
                    print("No es posible, el stock máximo es "+str(stock[i]), ", vuelva a iniciar el proceso.")
                else:  
                    comprobar=input(f"En su carrito tiene {self.cantidadProducto} {productos[i]}, ¿está seguro de su compra?: ")    
                    print()                                                                                                        
                    if comprobar.lower()=="si": 
                        self.paisCliente=input("Ingrese el país desde el que hace el pedido: ")
                        precioSinIVA=float(self.cantidadProducto)*precio[i] 
                        stockRestante=stock[i]-int(self.cantidadProducto)   
                        print(f"El precio sin IVA es {precioSinIVA}€, quedan {stockRestante} unidades en stock.")  
                        if self.paisCliente=="España":  
                            precioConIVA=precioSinIVA*1.21  
                            print(f"El total con el IVA es {precioConIVA:.2f}€.")   
                            print()
                            print(f"Se le ha mandado un PDF al correo electrónico.")    
                            print(f"Se le ha mandado un SMS al número de teléfono con el cual puede ver el seguimiento.")  
                            print(f"La fecha de envío es {fechaAleatoria} (Año-Mes-Día)")
                        elif self.paisCliente!="España":    
                            precioConIVA=precioSinIVA*(random.uniform(1,2))
                            print(f"El total con el IVA añadido de su respectivo país es {precioConIVA:.2f}€.") 
                            print()  
                            print(f"Se le ha mandado un PDF al correo electrónico.")
                            print(f"Se le ha mandado un SMS al número de teléfono con el cual puede ver el seguimiento.")
                            print(f"La fecha de envío es {fechaAleatoria} (Año-Mes-Día)")
                    else:
                        print("Vuelva a iniciar el proceso para seleccionar los productos deseados.")  
                                                                                                       
            i=i+1  

producto1=Producto()    
producto1.productos()  