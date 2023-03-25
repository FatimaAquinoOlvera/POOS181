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
            
            
            
            
            
            
        
    
