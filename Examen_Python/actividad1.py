#actividad1
#Solicita por consola la respuesta a una pregunta.
#El usuario puede responder hasta que acierte.
#Muestra los intentos que ha necesitado
# total 5 puntos.
#la aplicación funciona correctamente : 1 punto
#muestra la fecha y hora de inicio del test y fecha y hora de fin test con formato coherente: 1 punto
#control de errores y validación. siempre indica que test ha finalizado 1 punto
#la respuesta está en un array 1 punto
#la respuesta está en un archivo txt externo 1 punto
from datetime import datetime

try:        #try evalua lo que está dentro.
    # inicio de test
    print('Comienza el test')
    fecha_inicio = datetime.now()
    fecha_inicio_format = fecha_inicio.strftime("%H:%M:%S")
    print(f'Fecha inicio de test {fecha_inicio_format}')

    # almacena en una variable de tipo string la respuesta
    respuesta = input('Dime la capital de Francia: ')
    intento = 1  # acumulador
    archivo = open('respuestas.txt', 'r')
    contenido = archivo.readline()
    while respuesta.lower() != contenido:
        print('has fallado. Vuelve a intentarlo')
        intento = intento + 1
        respuesta = input('Dime la capital de Francia: ')
    print('respuesta correcta')
    print(f'has necesitado {intento} intentos')

    fecha_fin = datetime.now()
    fecha_fin_format = fecha_fin.strftime("%H:%M:%S")
    print(f'Fecha fin de test {fecha_fin_format}')
except: #Si algo falla en el try se ejecuta el except.
    print('algo va mal')
finally:    #Si todo ha funcionado bien se ejecuta esto.
    print('fin test. haya ido bien o mal.')

