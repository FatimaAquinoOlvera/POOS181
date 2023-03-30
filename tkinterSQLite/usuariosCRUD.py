from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from controladorBD import * #1. Presentamos los archivos vontrolador vista

#2. Creamos un objeto de la clase controladorBD
controlador= controladorBD()

#3. Funcion para disparar el objeto
def ejecutarInsert():
    controlador.guaradarUsuarios(varNom.get(),varCor.get(),varCon.get())
    
#4. Funcion para disparar el  boton de busqueda
def ejecutarSelectU():
    usuario = controlador.consultarUsuario(varBus.get())
    
    for usu in usuario:
        cadena=str(usu[0])+" "+ usu[1]+" "+ usu[2]+" "+str(usu[3]) 
    
    if(usuario):
        #print(cadena)
        textEnc.insert("0.0", cadena)
        
    else:
        messagebox.showinfo("Usuario no encontrado","Usuario no existe en la base de datos")
        
        

Ventana=Tk()
Ventana.title("CRUD de usuario")
Ventana.geometry("500x300") 

panel = ttk.Notebook(Ventana)
panel.pack(fill='both',expand='yes')

pestana1= ttk.Frame(panel)
pestana2= ttk.Frame(panel)
pestana3= ttk.Frame(panel)
pestana4= ttk.Frame(panel)

#Pestaña 1: Formulario de usuarios.

titulo = Label (pestana1, text="Registro de usuarios", fg='blue', font=("Modern", 18)).pack()

varNom= tk.StringVar() #Variables para poder almacenar los valores de entry 
lblNom= Label(pestana1, text="Nombre").pack()
txtNom= Entry(pestana1, textvariable=varNom).pack()


varCor= tk.StringVar()
lblCor= Label(pestana1, text="Correo").pack()
txtCor= Entry(pestana1, textvariable=varCor).pack()

varCon= tk.StringVar()
lblCon= Label(pestana1, text="Contraseña").pack()
txtCon= Entry(pestana1, textvariable=varCon).pack()

btnGuardar= Button(pestana1, text="Guardar usuario",command=ejecutarInsert).pack()

#Pestaña 2: Buscar Usuarios 
titulo2 = Label (pestana2, text="Buscar usuarios", fg='green', font=("Modern", 18)).pack()

varBus= tk.StringVar() 
lblLid= Label(pestana2, text="Identificador de Usuario").pack()
txtid= Entry(pestana2, textvariable=varBus).pack()
btnBus= Button(pestana2, text="Buscar",command=ejecutarSelectU).pack()

subBus= Label(pestana2, text="Encontrado",fg='blue', font=("Modern", 18)).pack()
textEnc=tk.Text(pestana2, height=5,width=52)
textEnc.pack()


panel.add(pestana1, text='Formulario de usuario')
panel.add(pestana2, text='Buscar usuario')
panel.add(pestana3, text='Consultar usuario')
panel.add(pestana4, text='Actulizar usuario')


Ventana.mainloop()



