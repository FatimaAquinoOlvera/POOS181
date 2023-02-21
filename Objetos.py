#1. Importar la clase
from personaje import *

#2. Instanciar un objeto
Heroe = Personaje()

#3. Acceder a sus atriutos

print("El personaje pertenece a la raza: "+ Heroe.especie)
print("Se llama: "+ Heroe.nombre)
print("El personaje mide: "+ str(Heroe.altuta) + "metros")


#4. Acceder a los metodos

Heroe.correr(True)
Heroe.LanazarGranada()
Heroe.RecargaArma(68)
