
class Personaje:
    
    #Atributos del personaje
    especie= "humano"
    nombre= "Lalo fenix"
    altuta= 1.90
    
    #Metodos personajes
    
    def correr(self,status):
        if (status):
            print("El personaje "+ self.nombre+ "Esta corriendo ")
        else:
             print("El personaje "+ self.nombre +"Se detuvo")
             
    def LanazarGranada(self):
         print("Se lanzo granada")
         
    def RecargaArma(self, municiones):
         cargador=5
         cargador=cargador+municiones
         print("El arma tiene ahora"+cargador+"balas")
         
         
         
