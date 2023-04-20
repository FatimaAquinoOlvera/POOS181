from tkinter import messagebox
import sqlite3

class ControladorBD:
    def __init__(self):
        pass
    
    #Metodo crear conexiones
    def conexionBD(self):
        try:
            conexion = sqlite3.connect("BDImportaciones.db")
            print("Conectado con exito")
            return conexion
        except sqlite3.OperationalError:
            print("Fallo en la conexion")

    #Metodo para ingresar mercancia
    def ingresar(self, mercancia, pais):
        conx = self.conexionBD()
        cursor = conx.cursor()
        try:
            cursor.execute("insert into TB_Europa(Mercancia, Pais) values(?,?)", (mercancia, pais))
            conx.commit()
            conx.close()
            messagebox.showinfo("EXITO", "Se guardo la mercancia")
        except:
            messagebox.showerror("ERROR", "No se pudo guardar la mercancia")
            conx.close()
            return

