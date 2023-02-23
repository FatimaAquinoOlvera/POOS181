
class Personaje:
    
    def __init__(self, esp,nom,alt):   
        self.especie= esp
        self.nombre= nom
        self.altura= alt
        
    #Metodos personajes
    
    def correr(self,status):
        if (status):
            print("El personaje "+ self.nombre + " esta corriendo ")
        else:
             print("El personaje "+ self.nombre +"se detuvo")
             
    def LanazarGranada(self):
         print("Se lanzo granada")
         
    def RecargaArma(self, municiones):
        cargador = 5
        cargador = cargador + municiones
        print("El arma tiene ahora" + str(cargador) + "balas")
         
         
         
