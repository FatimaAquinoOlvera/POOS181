from practica12 import Login 
import tkinter as va

# Main de ejecucion de la ventana

def main(): # Función llamada "main"
    root = va.Tk() # Crea la ventana principal de la aplicación ("root" es el objeto de la ventana).
    lo = Login(root) # Instancia de la clase "Login" y le pasa el objeto "root".
    root.mainloop() # Bucle infinito.
main() # Llama a la función "main".
