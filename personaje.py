
class Personaje:
    
    def __init__(self, esp,nom,alt):   
        self.__especie= esp
        self.__nombre= nom
        self.__altura= alt
        
    #Metodos personajes
    
    def correr(self,status):
        if (status):
            print("El personaje "+ self.__nombre + " esta corriendo ")
        else:
             print("El personaje "+ self.__nombre +"se detuvo")
             
    def LanazarGranada(self):
         print("Se lanzo granada")
         
    def RecargaArma(self, municiones):
        cargador = 5
        cargador = cargador + municiones
        print("El arma tiene ahora" + str(cargador) + "balas")
        
    #Ejemplo de metodo privado
    #def __pensar(self):
        #print ("Estoy pensando...")
        
    #Declaramos los getters y setters de los atributos en privado
        
    def getEspecie(self):
        return self.__especie
    
    def setEspecie(self,esp):
        self.__especie = esp
        
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self,nom):
        self.__nombre = nom
        
    def getAltura(self):
        return self.__altura
    
    def setAltura(self,alt):
        self.__altura = alt
    
    
    


        
         
         
         
         
