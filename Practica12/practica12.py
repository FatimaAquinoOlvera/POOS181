from tkinter import * # Esto importa todas las clases y funciones de la biblioteca Tkinter.
from tkinter import messagebox

class Login: #Esto define una clase llamada Login.
    def __init__(self, master): # Es el constructor de la clase "Login" que recibe un argumento master, que representa la ventana principal de la aplicación.
        self.master = master #Almacena la ventana principal en una variable de instancia llamada master.
        master.title("Login") #título de la ventana principal en "Login".
       
        # Etiquetas
        self.label_email = Label(master, text="Email:")
        self.label_email.grid(row=0, column=0, sticky=E) #sticky E = posicion este
        
        self.label_password = Label(master, text="Password:")
        self.label_password.grid(row=1, column=0, sticky=E)
        
        # Cuadros de texto (Entrada de texto )
        self.entry_email = Entry(master)
        self.entry_email.grid(row=0, column=1)

        self.entry_password = Entry(master, show="*") #caracteres de la contraseña se muestren como asteriscos.
        self.entry_password.grid(row=1, column=1)
       
        # Botones
        self.button_login = Button(master, text="Login", command=self.login) #se ejecutará cuando se haga clic en el botón.
        self.button_login.grid(row=2, column=1)
        

        # Define una función.
    def login(self):
        email = self.entry_email.get() # obtiene el valor ingresado por el usuario.
        password = self.entry_password.get() 
            
        # Validar si la contraseña o correo.
        if not email or not password:
            messagebox.showerror("Error", "Se requiere correo electrónico y contraseña.") #Esta vacio. 
        elif email == "example@upq.mx" and password == "password":
            messagebox.showinfo("Éxito", "Bienvenido!") #Esta correcto.
        else:
            messagebox.showerror("Error", "Correo electrónico o contraseña no válidos.") #Esta incorrecto.

       
