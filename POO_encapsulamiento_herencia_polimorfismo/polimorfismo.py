#https://ellibrodepython.com/polimorfismo-en-programacion

#método, tiene una respuesta diferente en función del obeto que le llame.
#sobrecarga de métodos: suele estar relacionado.

#método(argumento, argumento=None): #Python soporta argumentos con valores predeterminados
#Python no soporta sobrecarga com0o en otros lenguajes

#sobrecarga (overload)
def comer(quien,que,donde="en tu casa"):    #ejemplo de sobrecarga (overload)
    print(f"{quien} está comiendo {que} {donde}")
#ejemplo de polimorfismo
comer("laura","chuletas")
comer("pepe","solomillo","en un bar")   #uso es como sobrecarga, pero Python NO lo soporta

#polimorfismo en las clases
class Estudiante():
    def hacerExamen(self): #self para métodos de instancia
        print("El examen es teórico de 20 preguntas tipo test")

class GradoMedio(Estudiante):
    pass

class GradoSuperior(Estudiante):
    def hacerExamen(self):  #sobreescritura
        print("El examen es práctico y se entrega en PDF")

class DobleCiclo(Estudiante):
    def hacerExamen(self):  #sobreescritura
        print("El examen es práctico y ordinario")

alumno1=GradoMedio()
alumno2=GradoSuperior()
alumno3=DobleCiclo()
alumno4=GradoSuperior()
alumno5=GradoMedio()

convocatoria=[alumno1,alumno2,alumno3,alumno4,alumno5]
for alumno in convocatoria:
    alumno.hacerExamen()    #polimorfismo