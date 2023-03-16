#Se importa datetime para obtener el año actual y random para generar un numero aleatorio
import datetime
import random
from tkinter import messagebox


#Se crea la clase Logica
class Logica:
    #Se crea el constructor que obtiene los datos de la Interfaz
    def _init_(self, nombre, apellidoPaterno, apellidoMaterno, anioNacimiento, carrera):
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.anioNacimiento = anioNacimiento
        self.carrera = carrera
        self.generarMatricula()

    def generarMatricula(self):
        #Se obtiene el año actual
        self.anioActual = datetime.datetime.now().year
        self.anioActual = str(self.anioActual)
        #Se genera un numero aleatorio de 2 digitos entre el 10 y el 99
        self.numeroAleatorio = random.randint(10, 99)

        #Se convierten los valores a cadenas para poder concatenarlos
        #Se toma solo la primera letra del nombre
        self.nombre = str(self.nombre[0])
        #Se toma solo las 2 primeras letras del apellido paterno
        self.apellidoPaterno = str(self.apellidoPaterno[0:1])
        #Se toma solo las 2 primeras letras del apellido materno
        self.apellidoMaterno = str(self.apellidoMaterno[0:1])
        #Se toma solo las 2 ultimas letras del año de nacimiento
        self.anioNacimiento = str(self.anioNacimiento[-2:])
        #Se toma solo las 2 ultimos digitos del año actual
        self.anioActual = str(self.anioActual[-2:])
        #Se toma solo las 3 primeras letras de la carrera
        self.carrera = str(self.carrera[0:2])
        #Se convierte el numero aleatorio a cadena
        self.numeroAleatorio = str(self.numeroAleatorio)

        #Se genera la matricula
        self.matricula = self.nombre + self.apellidoPaterno + self.apellidoMaterno + self.anioNacimiento + self.anioActual + self.carrera + self.numeroAleatorio
        #Se imprime la matricula con un messagebox
        messagebox.showinfo("Matricula", self.matricula)