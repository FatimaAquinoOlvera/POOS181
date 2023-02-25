#1. Importar la clase
from personaje import *

#2.Solicitar los atributos par el objeto
print("")
print("## Solicitud de los datos del heroe ###")
espH= input ("Escribe la especie del heroe ")
nomH= input ("Escribe el nombre del heroe ")
altH= float(input( "Escribe la altura del heroe "))
cargaH= int(input ("Cuantas balas se recargaran al heroe "))


print("")
print("## Solicitud de los datos del villano ### ")
espV= input ("Escribe la especie del villano ")
nomV= input ("Escribe el nombre del villano ")
altV= float (input ("Escribe la altura del villano "))
cargaV= int (input ("Cuantas balas se recargaran al villano "))

#3. Creamos 2 objetos
Heroe = Personaje(espH,nomH,altH)
villano = Personaje(espV,nomV,altV)

#Ejemplo del uso de set
Heroe.setNombre("pepe pecas")

#4. Acceder a sus atriutos y metodos de cada objeto

print("")
print("##Atributos y Metodos de heroe")
print("El personaje pertenece a la raza: "+ Heroe.getEspecie())
print("Se llama: "+ Heroe.getNombre())
print("El personaje mide: "+ str(Heroe.getAltura()) + "metros")

Heroe.correr(True)
Heroe.LanazarGranada()
Heroe.RecargaArma(cargaH)

#Ejemplo de lo que no se puede hacer
#Heroe.__pensar()

print("")
print("##Atributos y Metodos de villano")
print("El personaje pertenece a la raza: "+ villano.getEspecie())
print("Se llama: "+ villano.getNombre())
print("El personaje mide: "+ str(villano.getAltura()) + "metros")


villano.correr(True)
villano.LanazarGranada()
villano.RecargaArma(cargaV)