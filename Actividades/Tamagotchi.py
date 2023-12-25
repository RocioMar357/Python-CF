

class Tamagotchi():
    def __init__(self,nombre,nivel_energia=100,nivel_hambre=0,nivel_felicidad=50,humor= "eufórico",esta_vivo=True):
        self.nombre = nombre
        self.nivel_energia = nivel_energia
        self.nivel_hambre = nivel_hambre
        self.nivel_felicidad = nivel_felicidad
        self.humor = humor
        self.esta_vivo = esta_vivo
        
def mostrar_estado(self):
    print(self.nombre)
    print(self.nivel_energia)
    print(self.nivel_hambre)
    print(self.humor)
def alimentar(self):
    if self.nivel_hambre > 10:
        self.nivel_hambre -= 10
    else:
        self.nivel_hambre = 0
    if self.nivel_energia > 15:
        self.nivel_energia -= 15
    else:
        self.nivel_energia = 0
        self.esta_vivo = False
            
def jugar(self):
    if self.nivel_hambre == 20:
        if self.nivel_energia > 20:
            self.nivel_energia -= 20
        else:
                self.nivel_energia = 0
        if nivel_felicidad < 30:
            nivel_felicidad -= 30
        else: 
            nivel_felicidad = 0
        if self.nivel_energia == 0:
            self.esta_vivo = False
    else:
        
        if nivel_felicidad < 30:
            nivel_felicidad += 20
        else: 
            nivel_felicidad = 50
        if self.nivel_energia > 18:
            self.nivel_energia -= 18
        else:
            self.nivel_energia = 0
            self.esta_vivo = False
                
        if self.nivel_hambre < 10:
            self.nivel_hambre += 10
        else: 
            self.nivel_hambre = 20
        
def dormir(self):
    
    if self.nivel_hambre == 20:
        if self.nivel_energia > 20:
            self.nivel_energia -= 20
        else:
                self.nivel_energia = 0
        if nivel_felicidad < 30:
            nivel_felicidad -= 30
        else: 
            nivel_felicidad = 0
        if self.nivel_energia == 0:
            self.esta_vivo = False
    else:
        
        if self.nivel_energia < 60:
            self.nivel_energia += 40
        else:
            self.nivel_energia = 100
        
        if self.nivel_hambre < 15:
            self.nivel_hambre += 5
        else: 
            self.nivel_hambre = 20
        
def Verificar_estado(self):
    if self.esta_vivo == True:
        print("Esta vivo")
    else:
        print("Esta muerto")    