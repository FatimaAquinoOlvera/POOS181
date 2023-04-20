from tkinter import messagebox
import sqlite3

class ControladorBD:
    def __init__(self):
        pass
    
    #Metodo crear conexiones
    def conexionBD(self):
        try:
            conexion = sqlite3.connect("C:/Users/Sistemas/Documents/POOS181/Examen3/BDImportaciones.db")
            print("Conectado con exito")
            return conexion
        except sqlite3.OperationalError:
            print("Fallo en la conexion")

    def registar(self, mercancia, pais):
        # Se comprueba que los campos no esten vacios
        if (mercancia == "" or pais == ""):
            messagebox.showwarning("CUIDADO", "Revisa tus datos, uno o mas campos estan vacios")
            return

        #Procedimiento para guardar la mercancia en la base de datos
        conx = self.conexionBD()
        cursor = conx.cursor()
        try:
            #Se intenta guardar la mercancia
            cursor.execute("insert into TB_Europa(Mercancia, Pais) values(?,?)", (mercancia, pais))
            conx.commit()
            conx.close()
            messagebox.showinfo("EXITO", "Se guardo la mercancia")
        except:
            #Si no se puede guardar la mercancia se muestra un mensaje de error
            messagebox.showerror("ERROR", "No se pudo guardar la mercancia")
            conx.close()
            return

    def consultar(self, pais):
        if (pais == ""):
            messagebox.showwarning("CUIDADO", "El campo pais esta vacio")
            return
        #Procedimiento para consultar la mercancia en la base de datos
        conx = self.conexionBD()
        cursor = conx.cursor()
        try:
            #Se intenta consultar la mercancia
            cursor.execute("SELECT * FROM TB_Europa WHERE Pais = ?", (pais,))
            mercancia = cursor.fetchall()
            conx.close()
            # Comprobar si la mercancia existe
            if len(mercancia) == 0:
                # Si la mercancia no existe se retorna None y se muestra un mensaje de error
                messagebox.showwarning("Error", "La mercancia con ese pais no existe")
                return
            return mercancia
        except:
            #Si no se puede consultar la mercancia se muestra un mensaje de error
            messagebox.showerror("ERROR", "No se pudo consultar la mercancia")
            conx.close()
            return

    def eliminar(self, id):
        # Se comprueba que id no esten vacio
        if (id == ""):
            messagebox.showwarning("CUIDADO", "El campo id esta vacio")
            return
        #Procedimiento para eliminar la mercancia en la base de datos
        conx = self.conexionBD()
        cursor = conx.cursor()
        try:
            #Comprobar si la mercancia existe
            cursor.execute("SELECT * FROM TB_Europa WHERE IDImpo = ?", (id,))
            mercancia = cursor.fetchall()
            if len(mercancia) == 0:
                # Si la mercancia no existe se retorna None y se muestra un mensaje de error
                messagebox.showwarning("Error", "La mercancia con ese id no existe")
                conx.close()
                return
            #Se intenta eliminar la mercancia
            cursor.execute("DELETE FROM TB_Europa WHERE IDImpo = ?", (id,))
            conx.commit()
            conx.close()
            messagebox.showinfo("EXITO", "Se elimino la mercancia")
        except:
            #Si no se puede eliminar la mercancia se muestra un mensaje de error
            messagebox.showerror("ERROR", "No se pudo eliminar la mercancia")
            conx.close()
            return

 