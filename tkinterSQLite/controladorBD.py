from tkinter import messagebox
import sqlite3
import bcrypt

class controladorBD: 
    
    def __init__(self):
        pass
    
    #Metodo crear conexiones
    def conexionBD(self):
        
        try:
            conexion=sqlite3.connect("C:/Users/Sistemas/Documents/POOS181/tkinterSQLite/DBUsuarios.db")
            print("Conectado a la BD")
            return conexion
        except sqlite3.OperationalError:
            print("No se puso conectar a la Bd")
        
    #Metodo para guardar usuarios
    
    def guaradarUsuarios(self,nom,cor,con):
        
        #1. usamos conexion
        conx=self.conexionBD()
        
        #2.validar parametros vacios
        if(nom=="" or cor=="" or con==""):
            messagebox.showwarning("Cuidado","Formulario incompleto")
        else: 
            
            #3. Preparar el cursosr, datos incertar, QuerySQL
            cursor=conx.cursor()
            conH= self.encriptarCon(con)
            datos=(nom,cor,conH)
            qrInsert="insert into TBRegistrados(Nombre,Correo,Contra)values (?,?,?)"
            
            #4. Ejecutar Insert y cerramos Conexion
            cursor.execute(qrInsert,datos)
            conx.commit() #Envia cambios a la base de datos.
            conx.close()
            messagebox.showinfo("Exito","Usuario Guardado")
            
    # Metodo para encriptar contraseñas      
    def encriptarCon(self,con):
        conPlana=con
        
        #Preparamos con en bytes y la SAL
        conPlana= conPlana.encode() #convertimos con a bytes
        sal=bcrypt.gensalt() 
        
        #Encriptamos la contraseña
        conHa=bcrypt.hashpw(conPlana,sal) #hashpw crea la contraseña encriptada
        print(conHa)
        
        #Enviamos la contraseña encriptada
        return conHa
            
    # Metodo para buscar 1 usuario 
    def consultarUsuario(self,id): 
        #1. Preparar Conexion 
        conx= self.conexionBD()
        
        #2. Verificar si id contiene algo
        if(id == ""):
            messagebox.showwarning("Cuidado","Id vacio escribe algo valido")  
            conx.close()     
            
        else:
            try:
                #3. Preparar cursor y el query
                cursor=conx.cursor()
                selectQry= "select * from TBRegistrados where id="+id
                
                #4. Ejecutar y guardar la consulta
                cursor.execute(selectQry)
                rsUsuario= cursor.fetchall()
                conx.close()
                
                return rsUsuario
                        
            except sqlite3.OperationalError:
                print("Error consulta")    
            
    # Practica 17
    # Método para obtener todos los usuarios de la tabla Registrados
    def obtenerUsuarios(self):
        # 1. Usamos conexion
        conx = self.conexionBD()

        # 2. Preparar el cursor y la consulta SQL
        cursor = conx.cursor()
        qrSelect = "SELECT * FROM TBRegistrados"

        # 3. Ejecutar la consulta y obtener los usuarios
        cursor.execute(qrSelect)
        usuarios = cursor.fetchall()

        # 4. Cerrar la conexión y devolver los usuarios
        conx.close()
        return usuarios
     
    # Practica 18
    # Método para Actualizar Usuario
    def actualizarUsuario(self, id, nombre, correo, contra):
            try:
                conexion = self.conexionBD()
                cursor = conexion.cursor()
                salt = bcrypt.gensalt()
                contra = bcrypt.hashpw(contra.encode('utf-8'), salt)
                cursor.execute('''UPDATE TBRegistrados SET nombre=?, correo=?, contra=? WHERE id=?''', (nombre, correo, contra, id))
                conexion.commit()
                messagebox.showinfo("Actualización", "El usuario se ha actualizado correctamente")
            except sqlite3.Error as error:
                messagebox.showerror("Error en la actualización", "Error en la base de datos: " + str(error))
            finally:
                if conexion:
                    conexion.close()
                    
    # Método para Eliminar Usuario
    def eliminarUsuario(self, id):
        try:
            conexion = self.conexionBD()
            cursor = conexion.cursor()
            
            # Obtener información del usuario a eliminar
            cursor.execute('''SELECT nombre, correo FROM TBRegistrados WHERE id=?''', (id,))
            usuario = cursor.fetchone()
            
            # Confirmar la eliminación con el usuario
            confirmacion = messagebox.askyesno("Confirmación", f"¿Está seguro de eliminar al usuario '{usuario[0]}' con correo '{usuario[1]}'?")
            
            if confirmacion:
                # Eliminar al usuario
                cursor.execute('''DELETE FROM TBRegistrados WHERE id=?''', (id,))
                conexion.commit()
                messagebox.showinfo("Eliminación", "El usuario se ha eliminado correctamente")
            else:
                messagebox.showinfo("Eliminación cancelada", "La eliminación del usuario ha sido cancelada.")
                
        except sqlite3.Error as error:
            messagebox.showerror("Error en la eliminación", "Error en la base de datos: " + str(error))
        finally:
            if conexion:
                conexion.close()
                
                
                