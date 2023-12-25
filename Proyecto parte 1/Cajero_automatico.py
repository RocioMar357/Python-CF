
def registrarse(Lista_cuenta):
    condicion = True
    while condicion == True:
        usuario = input("Ingrese su usuario: ")
        if Lista_cuenta != []:
            for i in Lista_cuenta:
                
                if i[0][0] == usuario:
                    print("Usuario ya existente, ingrese con otro usuario")
                    condicion = True
                    break
                else:
                    condicion = False
        else: 
            condicion = False        
    lista_usuario = []

    clave = input("Ingrese contraseña : ")

    tupla_usuario = (usuario,clave)

    lista_usuario.append(tupla_usuario)
    lista_usuario.append(10000)
    
    Lista_cuenta.append(lista_usuario)
    

"""
Bienvenido:
Cajero Automatico Express
"""
"""
MENU:
1) Ingresar dinero
2) Retirar dinero
3) Consultar Saldo 
4) Transferencias
5) salir
"""   

seguir_usando = True

Lista_cuenta = []
while seguir_usando == True:
    
    if Lista_cuenta == []:
        print("La lista de cuentas esta vacia, registre un usuario: ")
        registrarse(Lista_cuenta)
    else:
        opcion = int(input("Si desea registrar, marque 1. Si quiere iniciar sesion , marque 2: "))
        if opcion == 1:
            registrarse(Lista_cuenta)
        else:    
            condicion = True
            while condicion == True:
                usuario = input("Ingrese su usuario: ")
                clave = input("Ingrese su clave: ")
                
                for i in Lista_cuenta:
                    
                    if i[0][0] == usuario:
                        
                        if i[0][1] == clave:
                            condicion = False
                            cuenta = i
                            break
                        else:
                            print("Clave incorrecta")
                            break
                if condicion == True:
                    print("Usuario incorrecto")
                    
            print("1. ingresar dinero")
            print("2. Retirar dinero")
            print("3. Consultar saldo")
            print("4. Transferencias")
            print("5. Salir")
            opcion = int(input("Ingrese opcion: "))
            
            if opcion == 1:
                ingresar = int(input("Ingrese dinero: "))
                cuenta[1] = cuenta[1] + ingresar
                
            elif opcion == 2:
                condicion = True
                while condicion == True:
                    retirar = int(input("Cuanto dinero quiere retirar: "))
                    if retirar > cuenta[1]:
                        print("Dinero insuficiente , usted tiene ",cuenta[1])
                    else:
                        condicion = False
                cuenta[1] = cuenta[1] - retirar
            elif opcion == 3:
                print("Usted tiene: ", cuenta[1])
                
            elif opcion == 4:
                usuario_tran = input("Ingrese al usuario al que quiere tranferirle: ")
                existe = False
                
                for i in Lista_cuenta:
                    
                    if i[0][0] == usuario_tran:
                        condicion = True
                        while condicion == True:
                            retirar = int(input("Cuanto dinero quiere transferir?: "))
                            if retirar > cuenta[1]:
                                print("Dinero insuficiente , usted tiene ",cuenta[1])
                            else:
                                condicion = False
                        cuenta[1] = cuenta[1] - retirar
                        i[1] = i[1] + retirar
                        existe = True
                        break
                if existe == False:    
                    print("El usuario al que quiere transferir no existe")
                    
            else:
                seguir_usando = False
            







