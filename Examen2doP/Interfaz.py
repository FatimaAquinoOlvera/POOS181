from tkinter import *
from tkinter import messagebox

from Logica import Logica

class Interfaz:
    def __init__(self, ventana):
        self.ventana = ventana
        #Se inician los valores y se le da un titulo a la ventana
        ventana.title("Interfaz de usuario")
        ventana.geometry("400x400")

        #Se crean los elementos de la ventana y widgets

        #label del titulo
        self.label = Label(ventana, text="Generar matricula")
        self.label.pack()
        self.Label2 = Label(ventana, text="Datos a ingresar")
        self.Label2.pack()

        #label del nombre y su entrada de texto
        self.label_nombre = Label(ventana, text="Nombre:")
        self.label_nombre.pack()
        self.nombre = Entry(ventana)
        self.nombre.pack()

        #label de los apellidos y su entrada de texto
        self.label_appelidoPat = Label(ventana, text="Apellido Paterno:")
        self.label_appelidoPat.pack()
        self.appelidoPat = Entry(ventana)
        self.appelidoPat.pack()

        #Apellido materno
        self.label_appelidoMat = Label(ventana, text="Apellido Materno:")
        self.label_appelidoMat.pack()
        self.appelidoMat = Entry(ventana)
        self.appelidoMat.pack()

        #Fecha de nacimiento
        self.label_nacimiento = Label(ventana, text="Año de nacimiento:")
        self.label_nacimiento.pack()
        self.Nacimiento = Entry(ventana)
        self.Nacimiento.pack()

        #Carrera
        self.label_carrera = Label(ventana, text="Carrera:")
        self.label_carrera.pack()
        self.carrera = Entry(ventana)
        self.carrera.pack()

        #Boton para generar la matricula
        self.open_button = Button(ventana, text="Generar", command=self.generarMatricula)
        self.open_button.pack()

    def generarMatricula(self):
        #Comprueba que los campos no esten vacios
        if self.nombre.get() == "" or self.appelidoPat.get() == "" or self.appelidoMat.get() == "" or self.Nacimiento.get() == "" or self.carrera.get() == "":
            messagebox.showerror("Error", "No se pueden dejar campos vacios")
            return
        #Mada a llamar la clase Logica para generar la matricula
        self.logica = Logica(self.nombre.get(), self.appelidoPat.get(), self.appelidoMat.get(), self.Nacimiento.get(), self.carrera.get())



#Sentencia que carga la ventana principal
if __name__ == '__main__':
    #Se crea la ventana principal
    Principal = Tk()
    #Se crea la instancia de la clase Interfaz
    my_menu = Interfaz(Principal)
    #Se ejecuta el metodo mainloop() para que la ventana se mantenga abierta
    Principal.mainloop()