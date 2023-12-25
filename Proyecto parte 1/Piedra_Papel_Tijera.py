
from random import *
condicion = True

while condicion == True:
    respuesta = input("Desea jugar una partida :")
    if respuesta == "si" or respuesta == "SI":
        random = randint(1,3)
        print("La pc eligio ",random)
        """
        MENU DE OPCIONES:
        1) Tijera
        2) Papel
        3) Piedra
        """
        partida = int(input("Escoja su jugada: "))
        print("partida es igual a : ",partida)
        if random == 1:
            print("entre en 1 y partida es: ",partida)
            if partida == 1 :
                print("Empate")
            elif partida == 2:
                print("Jugada perdida")
            elif partida == 3:
                print("Jugada ganada")
        elif random == 2:
            print("entre en 2 y partida es: ",partida)
            if partida == 2 : 
                    print("Empate")
            elif partida == 3:
                print("Jugada perdida")
            elif partida == 1:
                print("Jugada ganada")
        else: 
            if random == 3:
                print("entre en 3 y partida es: ",partida)
                if partida == 3:
                    print("Empate")
                elif partida == 2:
                    print("Jugada perdida")
                elif partida == 1:
                    print("Jugada ganada") 
    else: 
        condicion = False
        print("Partida Finalizada")
