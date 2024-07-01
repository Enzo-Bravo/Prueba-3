import pruebas
lista=[["id"],["Nombre"],["Valorant"],["Fortnite"],["Fifa"],["Tipo"]]
op=2
juego=1
diccionario={"id",
            "Nombre",
            "Valorant",
            "Fortnite",
            "Fifa",
            "Tipo"}
while op!=4 and op<4 and op>0:
    print("----Bienvenido a eShirlitos----")
    print("1-Registrar puntajes del torneo")
    print("2-Listar todos los puntajes")
    print("3-Imprimir por tipo")
    print("4-Salir")
    while True:
        try:
            op=int(input("-->"))
            break
        except:
            print("Se espera un numero")
    if op==1:
        id=input("Ingrese su id:    ")
        lista[0].append(id)
        nombre=input("Ingrese su nombre y apellido:    ")
        lista[1].append(nombre)
        while juego!=4:
            print("1-Valorant")
            print("2-Fortnite")
            print("3-Fifa")
            print("4-Salir")
            while True:
                try:
                    juego=int(input("-->"))
                    if juego<5 and juego>0:
                        break
                    else:
                        print("Opcion no valida")
                except:
                    print("Se espera un numero")
            if juego==4:
                break
            while True:
                try:
                    puntaje=int(input("Ingrese su puntaje:  "))
                    break
                except:
                    print("Se espera un numero")
            if juego==1:
                lista[2].append(puntaje)
            elif juego==2:
                lista[3].append(puntaje)
            elif juego==3:
                lista[4].append(puntaje)
    elif op==2:
        print(diccionario)
    elif op==3:
        print()
    elif op==4:
        print("Saliendo")
    else:
        print("Opcion no valida")