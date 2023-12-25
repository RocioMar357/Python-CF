import random

class Personaje:
    def __init__(self,nombre,vida,ataque,defensa,inteligencia,agilidad,fuerza):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.inteligencia = inteligencia
        self.agilidad = agilidad
        self.fuerza = fuerza
        
    
    def atacar(self,enemigo):
        raise NotImplementedError("Método no implementado en la clase base")
    
    
class Guerrero(Personaje):
    danio_1 = 20
    danio_2 = 25
    arma_1 = "Martillo"
    arma_2 = "Hacha"
    def __init__(self,nombre): ## DEJA SOLO NOMBRE COMO parametro , el resto se especifica en cada clase 
        super().__init__(nombre,vida=250,ataque=30,defensa=80,inteligencia=15,agilidad=15,fuerza=75)
    
    def atacar(self,enemigo,arma):
        if enemigo.volar == True:
            opcion = random.randint(1,2)
            if opcion == 1:
                print("EL ENEMIGO ESQUIVO EL ATAQUE!")
            else:
                total_danio = self.fuerza + self.ataque + arma - (0.25*enemigo.defensa)
                enemigo.vida = enemigo.vida - total_danio
                print("Ataca a ",enemigo.nombre," y lo dejas con ",enemigo.vida," de vida")  
                
                
        else:
            total_danio = self.fuerza + self.ataque + arma - (0.25*enemigo.defensa)
            enemigo.vida = enemigo.vida - total_danio
            print("Ataca a ",enemigo.nombre," y lo dejas con ",enemigo.vida," de vida")
        
    
    def curar(self,jugador):
        jugador.vida = jugador.vida + 50
        print("Te has curado 50 de vida")
    
    
class Mago(Personaje):
    danio_1 = 25
    danio_2 = 30
    arma_1 = "Necromante"
    arma_2 = "Ignicion"
    def __init__(self,nombre):
        super().__init__(nombre,vida=150,ataque=15,defensa=20, inteligencia=70,agilidad=50,fuerza=10)
        
    def atacar(self,enemigo,arma):
        if enemigo.volar == True:
            opcion = random.randint(1,2)
            if opcion == 1:
                print("EL ENEMIGO ESQUIVO EL ATAQUE!")
            else:
                total_danio = self.inteligencia + self.ataque + arma - (0.25*enemigo.defensa)
                enemigo.vida = enemigo.vida - total_danio
                print("Ataca a ",enemigo.nombre," y lo dejas con ",enemigo.vida," de vida")  
                
                
        else:
            total_danio = self.inteligencia + self.ataque + arma - (0.25*enemigo.defensa)
            enemigo.vida = enemigo.vida - total_danio
            print("Ataca a ",enemigo.nombre," y lo dejas con ",enemigo.vida," de vida")
    
    def curar(self,jugador):
        jugador.vida = jugador.vida + 100
        print("Te has curado 100 de vida")
        
class Arquero(Personaje):
    danio_1 = 10
    danio_2 = 15
    arma_1 = "Arco"
    arma_2 = "Trampa"
    def __init__(self,nombre):
        super().__init__(nombre,vida=200 ,ataque=25 ,defensa=40 , inteligencia=50 ,agilidad=70,fuerza=50)
        
    def atacar(self,enemigo,arma):
        if enemigo.volar == True:
            opcion = random.randint(1,2)
            if opcion == 1:
                print("EL ENEMIGO ESQUIVO EL ATAQUE!")
            else:
                total_danio = self.agilidad + self.ataque + arma - (0.25*enemigo.defensa)
                enemigo.vida = enemigo.vida - total_danio
                print("Ataca a ",enemigo.nombre," y lo dejas con ",enemigo.vida," de vida")  
                
                
        else:
            total_danio = self.agilidad + self.ataque + arma - (0.25*enemigo.defensa)
            enemigo.vida = enemigo.vida - total_danio
            print("Ataca a ",enemigo.nombre," y lo dejas con ",enemigo.vida," de vida")
        
    
    def curar(self,jugador):
        jugador.vida = jugador.vida + 100
        print("Te has curado 100 de vida")
        
        
class Asesino(Personaje):
    danio_1 = 10
    danio_2 = 15
    arma_1 = "Espada"
    arma_2 = "Daga"
    def __init__(self,nombre):
        super().__init__(nombre,vida=100,ataque=80,defensa=35, inteligencia=50,agilidad=60,fuerza=30)
        
    def atacar(self,enemigo,arma):
        if enemigo.volar == True:
            opcion = random.randint(1,2)
            if opcion == 1:
                print("EL ENEMIGO ESQUIVO EL ATAQUE!")
            else:
                total_danio = self.inteligencia + self.agilidad + self.ataque + arma - (0.25*enemigo.defensa)
                enemigo.vida = enemigo.vida - total_danio
                print("Ataca a ",enemigo.nombre," y lo dejas con ",enemigo.vida," de vida")  
                
                
        else:
            total_danio = self.inteligencia + self.agilidad + self.ataque + arma - (0.25*enemigo.defensa)
            enemigo.vida = enemigo.vida - total_danio
            print("Ataca a ",enemigo.nombre," y lo dejas con ",enemigo.vida," de vida")
        
    
    def curar(self,jugador):
        jugador.vida = jugador.vida + 100
        print("Te has curado 100 de vida")
        
# class Enemigo(Personaje):
#     def __init__(self, nombre, volar=False):
#         super().__init__(nombre, vida=200, ataque=50, defensa=30, inteligencia=10, agilidad=15, fuerza=15)
#         self.volar = volar
        
#     def atacar(self,enemigo):
#         total_danio = self.fuerza + self.ataque  - (0.25*enemigo.defensa)
#         enemigo.vida = enemigo.vida - total_danio
#         print("Ataca a ",enemigo.nombre," y te deja con ",enemigo.vida," de vida")

# def curar(self,jugador):
#     jugador.vida = jugador.vida + 50
#     print("El enemigo se ha curado 50 de vida!")   

class Enemigo_guerrero(Personaje):
    def __init__(self, nombre, volar=False):
        super().__init__(nombre, vida=200, ataque=15, defensa=50, inteligencia=10, agilidad=15, fuerza=50)
        self.volar = volar
    def atacar(self,enemigo):
        total_danio = self.fuerza + self.ataque  - (0.25*enemigo.defensa)
        enemigo.vida = enemigo.vida - total_danio
        print("Ataca a ",enemigo.nombre," y te deja con ",enemigo.vida," de vida")
    def curar(self,jugador):
        jugador.vida = jugador.vida + 50
        print("El enemigo se ha curado 50 de vida!")
        
class Enemigo_mago(Personaje):
    def __init__(self, nombre, volar=False):
        super().__init__(nombre, vida=125, ataque=15, defensa=20, inteligencia=50, agilidad=40, fuerza=10)
        self.volar = volar
    def atacar(self,enemigo):
        total_danio = self.inteligencia + self.ataque  - (0.25*enemigo.defensa)
        enemigo.vida = enemigo.vida - total_danio
        print("Ataca a ",enemigo.nombre," y te deja con ",enemigo.vida," de vida")
    def curar(self,jugador):
        jugador.vida = jugador.vida + 100
        print("El enemigo se ha curado 100 de vida!")


class Enemigo_arquero(Personaje):
    def __init__(self, nombre, volar=False):
        super().__init__(nombre, vida=150, ataque=15, defensa=35, inteligencia=20, agilidad=70, fuerza=15)
        self.volar = volar
    def atacar(self,enemigo):
        total_danio = self.agilidad + self.ataque  - (0.25*enemigo.defensa)
        enemigo.vida = enemigo.vida - total_danio
        print("Ataca a ",enemigo.nombre," y te deja con ",enemigo.vida," de vida")
    def curar(self,jugador):
        jugador.vida = jugador.vida + 60
        print("El enemigo se ha curado 60 de vida!")

class Enemigo_asesino(Personaje):
    def __init__(self, nombre, volar=False):
        super().__init__(nombre, vida=100, ataque=15, defensa=30, inteligencia=40, agilidad=50, fuerza=15)
        self.volar = volar
    def atacar(self,enemigo):
        total_danio = self.inteligencia + self.agilidad + self.ataque  - (0.25*enemigo.defensa)
        enemigo.vida = enemigo.vida - total_danio
        print("Ataca a ",enemigo.nombre," y te deja con ",enemigo.vida," de vida")
    def curar(self,jugador):
        jugador.vida = jugador.vida + 75
        print("El enemigo se ha curado 75 de vida!")
        
        
def Elegir_enemigo(lista_enemigo):
    #print(lista_enemigo)
    numero = random.randint(0,len(lista_enemigo)-1)
    #print(numero)
    enemigo = lista_enemigo[numero]
    lista_enemigo.remove(enemigo)
    #print(lista_enemigo)
    return enemigo

def Arena_combate(jugador,arma,lista_enemigo):
    while len(lista_enemigo) > 0:
        if jugador.vida > 0:
            enemigo = Elegir_enemigo(lista_enemigo)
            print(" ")
            print("COMBATE ENTRE ",jugador.nombre," CONTRA EL ENEMIGO ",enemigo.nombre)
            
            while enemigo.vida> 0 and jugador.vida > 0:
                print(" ")
                print(jugador.nombre, "tiene", jugador.vida,"y", enemigo.nombre,"tiene ",enemigo.vida)
                if jugador.agilidad > enemigo.agilidad:
                    primero = jugador
                    juega_jugador = True
                else: 
                    primero = enemigo
                    juega_jugador = False
                
                if juega_jugador == True:
                    print(primero.nombre, "Ataca ")
                    print("Elija que quiere hacer: ")

                    print("1. Atacar ")
                    print("2. Curarse")
                    opcion = input("Elija su opcion: (1 o 2) ")
                    if opcion == "1":
                        jugador.atacar(enemigo,arma)
                    else:
                        jugador.curar(jugador)
                    if enemigo.vida > 0:
                        print("Turno de ",enemigo.nombre)
                            
                        opcion = random.randint(1,4)
                        if opcion == 1:
                            enemigo.curar(enemigo)
                        else:
                            enemigo.atacar(jugador) 
                        if jugador.vida < 0:
                            print("Te han matado")
                    else:
                        print("Has matado a ",enemigo.nombre)        
                else:
                    print("Ataca",enemigo.nombre)   
                    opcion = random.randint(1,4)
                    
                    if opcion == 1:
                        enemigo.curar(enemigo)
                    else:
                        enemigo.atacar(jugador)
                    if jugador.vida > 0:
                        
                        print("Turno de ",jugador.nombre)
                        print("Elija que quiere hacer: ")

                        print("1. Atacar ")
                        print("2. Curarse")
                        opcion = input("Elija su opcion: (1 o 2) ")
                        print("su opcion es ",opcion)
                        if opcion == "1":
                            jugador.atacar(enemigo,arma)
                        else:
                            jugador.curar(jugador)
                        if enemigo.vida < 0:
                            print("Has matado a ",enemigo.nombre)
                    else:
                        print("Te han matado")
    if jugador.vida > 0:
        print(" ")
        print("HAS GANADO LA ARENA DE COMBATE!!")                
                    
###PROGRAMA PRINCIPAL####

nombre_jugador = input("Ingresa el nombre de tu personaje: ")
clase_jugador = input("Selecciona tu clase (Guerrero, Mago, Arquero, Asesino): ")

if clase_jugador == "Guerrero":
    jugador = Guerrero(nombre_jugador)
elif clase_jugador == "Mago":
    jugador = Mago(nombre_jugador)
elif clase_jugador == "Arquero":
    jugador = Arquero(nombre_jugador)
elif clase_jugador == "Asesino":
    jugador = Asesino(nombre_jugador)
else:
    print("Clase no válida. Seleccionando Guerrero por defecto.")
    jugador = Guerrero(nombre_jugador)
    
print("Usted eligio un personaje de la clase: ",clase_jugador)

print("1. ",jugador.arma_1)
print("2. ",jugador.arma_2)
opcion = input("Elija su armamento: (1 o 2) ")

if opcion == 1:
    arma = jugador.danio_1
else:
    arma = jugador.danio_2
    
enemigo1 = Enemigo_guerrero("Orco Gigante")
enemigo2 = Enemigo_mago("Mago Oscuro Volador",volar=True)
enemigo3 = Enemigo_arquero("Arquero Veloz")
enemigo4 = Enemigo_asesino("Asesino Templario")

lista_enemigo = [enemigo1,enemigo2,enemigo3,enemigo4]
Arena_combate(jugador,arma,lista_enemigo)
