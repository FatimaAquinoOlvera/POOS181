from tkinter import Tk, Frame, Button, messagebox

#Funcion de mensajes
def mostraraMensaje():
    messagebox.showinfo("Aviso", "Este mensaje es para avisar algo")
    messagebox.showerror("Error:", "Todo fallo con exito")
    print (messagebox.askyesnocancel("Pregunta:", "El o ella jugo con tu corazon"))
    
#Funcion para agregar botones
def agregarBoton():
    botonMorado.config(text="+", bg="#33cc33", fg="#ffffff")
    botonNuevo= Button(seccion3, text="Boton Nuevo")
    botonNuevo.pack()
    
    
    

#1. Instanciamos un objeto ventana
ventana = Tk()
ventana.title("Practica 11: Frames")
ventana.geometry("600x400")

#2. Definimos secciones de la ventana 
seccion1 =Frame(ventana,bg="#ccddff")
seccion1.pack(expand=True, fill= 'both')

seccion2 =Frame(ventana,bg="#6699ff")
seccion2.pack(expand=True, fill= 'both')

seccion3 =Frame(ventana,bg="#ff80b3")
seccion3.pack(expand=True, fill= 'both')

#3. Botones
botonAzul = Button(seccion1, text="boton azul", fg="#002db3", command=mostraraMensaje)
botonAzul.place(x=60, y=60)

botonNegro = Button(seccion2, text="boton negro", fg="#000000")
botonNegro.grid(row=0, column=0)

botonRosa = Button(seccion2, text="boton rosa", bg="#ffffff", fg="#ff0066")
botonRosa.grid(row=0, column= 1)

botonMorado = Button(seccion3, text="boton morado", bg="#800080", command=agregarBoton)
botonMorado.pack()



# Main de ejecucion de la ventana
ventana.mainloop()


