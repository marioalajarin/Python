from datetime import datetime

#En consola aparecen tres opciones
#1. historia
#2. matemáticas
#3. química
#el usuario debe elegir una opción.
#si la pregunta es historia, le pregunta qué animal mató a Cleopatra
#si la pregunta es matemáticas, le pregunta cuál es el seno de 90
#si lapregunta es química, le pregunta cuál es el símbolo químico del potasio
#muestra cuánto tiempo ha tardado en realizar el test
#sólo se hace una pregunta
inicioTest=datetime.now()
inicioTestFormato=inicioTest.strftime("%H:%M:%S")
print(f"El examen empieza.   Hora:{inicioTestFormato}.")
asignaturas=["historia","matematicas","quimica"]
print(asignaturas)
asignatura=input("Escribe el nombre de una de estas asignaturas: ")


if asignatura in asignaturas:
    match asignatura:
        case "historia":
            animal=input("¿Qué animal mató a Cleopatra?: ")
            if animal == "serpiente":
                print("Es correcto")
            else:
                print("Es incorrecto")
        case "matematicas":
            seno=input("¿Cuánto es el seno de 90?: ")
            if seno == "1":
                print("Es correcto")
            else:
                print("Es incorrecto")
        case "quimica":
            simbolo=input("¿Cuál es el símbolo del potasio?: ")
            if simbolo == "K":
                print("Es correcto")
            else:
                print("Es incorrecto")
else:
    print("Esa opción no existe.")


finTest=datetime.now()
finTestFormato=finTest.strftime("%H:%M:%S")
print(f"El examen termina.   Hora:{finTestFormato}.")
