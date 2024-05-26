""""Simulacion del juego de priedra papel o tijera """

#Importamos ramdom que nos ayudara a elegir una de las tres opciones para la laptop
import random

#opciones que tenemos para elegir 
opciones = ["tijera", "papel", "piedra"]

#Haceos que el usuario eliga y creamos un dato ramdom para la computadora
usuario = input("Elige: ").lower()
lap= random.choice(opciones)

#Si el usuario no elige ninguna opcion mostrara error
if usuario not in opciones: 
    print("Error, ejige una opcion")
    quit()

#Si el usuario elige una opcion pero que sea igual que la lap es un empate 
if usuario == lap:
    print("Empate")
#Si, el usuario no debe cumplir alguna de esta condicion mostradas ya que seria un empate
elif usuario == "tijera" and lap  =="piedra" or usuario == "piedra" and lap =="papel" or usuario == "papel" and lap =="tijera":
    print("Has perdido")
#Si el usuario no cumple ninguna de estas condiciones, lo que quiere decir que ha ganado
else:
    print("Has ganado")
