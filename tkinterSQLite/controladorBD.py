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
            conx.close
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
     
            
        
    
