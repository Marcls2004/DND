import random
from Funciones_Rol.Funciones_menu import *
from Funciones_Rol.Variables_del_proyecto import  *

def clase(menu_clase,keys):
    while True:
        opc = gen_menu(menu_clase)
        print("Clase seleccionada {}".format(clases[keys[opc-1]]))
        input("Enter para continuar")
        return keys[opc-1]
#---------------------------------------------------------------CREAR HEROE---------------------------------------------------------------------
def nuevo_nombre_heroe():
    while True:
        print(nuevo_personaje)
        nombre = input("Nombre del personaje: ")
        if not nombre.isalpha():
            print(formato_invalido_letras)
        else:
            print("Nuevo nombre creado {}".format(nombre))
            input("Enter para continuar")
            return nombre

def ini_nivel():
    while True:
            new_nivel = input("Con que nivel quieres empezar la aventura? (1 - 5)\n")
            if not new_nivel.isdigit():
                print(formato_invalido_numeros)
            elif not int(new_nivel) in range(1,6):
                print("El nivel solo puede estar entre 1 y 5")
            else:
                return int(new_nivel)

def selec_arma(armas_dispo,keys):
    while True:
            opc = gen_menu(armas_dispo)
            
            print("Arma seleccionada {}.".format(armas[keys[opc-1]]["nombre"]))
            input("Enter para continuar")
            return keys[opc-1]
def selec_stats(stats):
    while stats[0] == 0 or stats[1] == 0 or stats[2] == 0 or stats[3] == 0 or stats[4] == 0:        
        print("estadisticas Actuales".center(40,"=") + "\nFuerza: {} Magia: {} Defensa: {} Agilidad: {} Vida: {}\n".format(stats[0], stats[1], stats[2], stats[3], stats[4]))
        opc = gen_menu(eleccion_estadisticas)
        if opc == 1:
            if stats[0] > 0:
                print("No puedes cambiar el destino.")
                input("Enter para continuar")
            else:
                dado = random.randint(10,20)
                print("La fuerza sera de {} puntos.".format(dado))
                input("Enter para continuar")
                stats[0] = dado
        elif opc == 2:
            if stats[1] > 0:
                print("No puedes cambiar el destino.")
                input("Enter para continuar")
            else:
                dado = random.randint(10, 20)
                print("La magia sera de {} puntos.".format(dado))
                input("Enter para continuar")
                stats[1] = dado
        elif opc == 3:
            if stats[2] > 0:
                print("No puedes cambiar el destino.")
                input("Enter para continuar")
            else:
                dado = random.randint(10, 20)
                print("La defensa sera de {} puntos.".format(dado))
                input("Enter para continuar")
                stats[2] = dado
        elif opc == 4:
            if stats[3] > 0:
                print("No puedes cambiar el destino.")
                input("Enter para continuar")
            else:
                dado = random.randint(10, 20)
                print("La agilidad sera de {} puntos.".format(dado))
                input("Enter para continuar")
                stats[3] = dado
        else:
            if stats[4] > 0:
                print("No puedes cambiar el destino.")
                input("Enter para continuar")
            else:
                dado = random.randint(10, 20)
                print("La vida sera de {} puntos.".format(dado))
                input("Enter para continuar")
                stats[4] = dado
    print("\n"+"Estadisticas Definitivos".center(40,"=") + "\nFuerza: {}\nMagia: {}\nDefensa: {}\nAgilidad: {}\nVida: {}\nCuenta que al subir de nivel sube entre un 3% - 12%".format(stats[0],stats[1],stats[2],stats[3],stats[4]))
    input("Enter para continuar")
    return stats

def mostrar_nuevo_heroe(nombre,clase,nivel,arma,stats):
    while True:
        if nivel > 1:
            for i in range(nivel):
                stats[0] = stats[0] * (1.0 + (random.randrange(30,140))/1000)
                stats[1] = stats[1] * (1.0 + (random.randrange(30,140))/1000)
                stats[2] = stats[2] * (1.0 + (random.randrange(30,140))/1000)
                stats[3] = stats[3] * (1.0 + (random.randrange(30,140))/1000)
                stats[4] = stats[4] * (1.0 + (random.randrange(30,140))/1000)
        
        stats[0] = int(stats[0])
        stats[1] = int(stats[1])
        stats[2] = int(stats[2])
        stats[3] = int(stats[3])
        stats[4] = int(stats[4])

        print(muestra_pers.format(nombre, clases[clase],nivel, armas[arma]["nombre"], stats[0], stats[1], stats[2], stats[3], stats[4]))
        opc = input("Quieres empezar la aventura? S/N\n")
        if opc.upper() != "S" and opc.upper() != "N":
            print("Tienes que poner una 'S' para aceptar o una 'N' para rechazar.")
            input("Enter para continuar")
        else:
            if opc.upper() == "N":
                print("Mala suerte la proxima intenta jugar con lo que te salga.")
                input("Enter para continuar")
                return ""
            else:
                print("Personaje creado")
                input("Enter para continuar")
                return {"nivel":nivel, "nombre": nombre, "clase":clase, "arma" : arma,
                                            "fuerza":stats[0], "magia":stats[1], "defensa":stats[2], "agilidad":stats[3],
                                            "vida":stats[4], "xp":0}
    

#---------------------------------------------------------------CREAR ARMA----------------------------------------------------------------------
def nuevo_nombre_arma():
    while True:
        nombre_arma = input("Nombre para l'arma:\n")
        probar_nombre = nombre_arma.replace(" ","")
        if not probar_nombre.isalpha():
            print(formato_invalido_letras)
        else:
            while True:
                nombre_igual = nombre_arma
                for i in range(len(armas)):
                    if armas[i + 1]["nombre"] == nombre_arma:
                        print("Este nombre ya existe.")
                        nombre_arma = input("Nombre para l'arma:\n")
                if nombre_igual == nombre_arma:
                    break
            print("Nuevo nombre creado {}".format(nombre_arma))
            input("Enter para continuar")
            return nombre_arma
        
def nuevas_estadisticas_arma():
    stats = {"características":[],"debuffo" : []}
    estadistica1 = 0
    nombre_estadistica1 = ""
    estadistica2 = 0
    nombre_estadistica2 = ""
    debuff = 0
    nombre_debuffo = ""
    while True: 
        if estadistica1 == 0 or estadistica2 == 0:
                opc = gen_menu(eleccion_estadisticas)
                if opc == 1 and nombre_estadistica1 != "fuerza":
                    if estadistica1 == 0:
                        nombre_estadistica1 = "fuerza"
                        estadistica1 = random.randint(1,6)
                    else:
                        nombre_estadistica2 = "fuerza"
                        estadistica2 = random.randint(1,6)

                elif opc == 2 and nombre_estadistica1 != "magia":
                    if estadistica1 == 0:
                        nombre_estadistica1 = "magia"
                        estadistica1 = random.randint(1,6)
                    else:
                        nombre_estadistica2 = "magia"
                        estadistica2 = random.randint(1,6)
                
                elif opc == 3 and nombre_estadistica1 != "defensa":
                    if estadistica1 == 0:
                        nombre_estadistica1 = "defensa"
                        estadistica1 = random.randint(1,6)
                    else:
                        nombre_estadistica2 = "defensa"
                        estadistica2 = random.randint(1,6)
                    
                elif opc == 4 and nombre_estadistica1 != "agilidad":
                    if estadistica1 == 0:
                        nombre_estadistica1 = "agilidad"
                        estadistica1 = random.randint(1,6)
                    else:
                        nombre_estadistica2 = "agilidad"
                        estadistica2 = random.randint(1,6)
                
                elif opc == 5 and nombre_estadistica1 != "vida":
                    if estadistica1 == 0:
                        nombre_estadistica1 = "vida"
                        estadistica1 = random.randint(1,6)
                    else:
                        nombre_estadistica2 = "vida"
                        estadistica2 = random.randint(1,6)
                else:
                    print("Esta característica ya la has elegido, elige otra.")
                    input("Enter para continuar")
        else:
            dec_deb = input("Quieres poner un debuff aleatorio? S/N \n(Si pones un debuff las estadistica tendran un aumento de un 50% en las estadisticas.\n" \
            "Pero el debuffo tembien sera de un aumento de 50%) ")
            if dec_deb.upper() == "S":
                estadistica1 = int(estadistica1 * 1.5)
                estadistica2 = int(estadistica2 * 1.5)
                estadistica_random = random.randint(1,5)

                if estadistica_random == 1:
                    nombre_debuffo = "fuerza"
                    debuff = -int(random.randint(1,6) * 1.5)
                
                elif estadistica_random == 2:
                    nombre_debuffo = "magia"
                    debuff = -int(random.randint(1,6) * 1.5)                 

                elif estadistica_random == 3:
                    nombre_debuffo = "defensa"
                    debuff = -int(random.randint(1,6) * 1.5)

                elif estadistica_random == 4:
                    nombre_debuffo = "agilidad"
                    debuff = -int(random.randint(1,6) * 1.5)

                else:
                    nombre_debuffo = "vida"
                    debuff = -int(random.randint(1,6) * 1.5)
                print("Las estadisticas del arma son:\n{} = {}\n{} = {}\n{} = {}".format(nombre_estadistica1, estadistica1, nombre_estadistica2, estadistica2, nombre_debuffo, debuff))
                input("Enter para continuar")
                break

            elif dec_deb.upper() == "N":
                print("Las estadisticas del arma son:\n{} = {}\n{} = {}\n".format(nombre_estadistica1, estadistica1, nombre_estadistica2, estadistica2))
                input("Enter para continuar")
                break

            else:
                print(formato_invalido_letras)
                input("Enter para continuar")
    
    stats["características"].append(nombre_estadistica1)
    stats["características"].append(estadistica1)
    stats["características"].append(nombre_estadistica2)
    stats["características"].append(estadistica2)
    stats["debuffo"].append(nombre_debuffo)
    stats["debuffo"].append(debuff)
    return stats
    
def final_arma_nueva(nombre,clase,estadisticas):
    while True:
        if estadisticas["debuffo"][0] == "":
            print("Esta es la nueva arma:\n" + muestra_arma.format(nombre, clases[clase], estadisticas["características"][0], estadisticas["características"][1], estadisticas["características"][2], estadisticas["características"][3]))
        
        else:
            print("Esta es la nueva arma:\n" + muestra_arma_deb.format(nombre, clases[clase], estadisticas["características"][0], estadisticas["características"][1], estadisticas["características"][2], estadisticas["características"][3]
                                                                       ,estadisticas["debuffo"][0],estadisticas["debuffo"][1]))

        opc = input("Quieres crear esta arma? S/N\n")
        if opc.upper() != "S" and opc.upper() != "N":
            print("Tienes que poner una 'S/s' para aceptar o una 'N/n' para rechazar.")
            input("Enter para continuar")
        else:
            if opc.upper() == "N":
                print("Mala suerte la proxima intenta jugar con lo que te salga.")
                input("Enter para continuar")
                flg_muestra = False
            else:
                print("Arma guardada en el arsenal")
                input("Enter para continuar")
                if estadisticas["debuffo"][0] == "": 
                    nueva_arma = {"clase" : clase, "nombre": nombre,
                                            "características":{estadisticas["características"][0] : estadisticas["características"][1], 
                                                               estadisticas["características"][2] : estadisticas["características"][3]}}
                    return nueva_arma
                else:
                    nueva_arma = {"clase" : clase, "nombre": nombre,
                                            "características":{estadisticas["características"][0] : estadisticas["características"][1], 
                                                               estadisticas["características"][2] : estadisticas["características"][3]},
                                            "debuffo":{estadisticas["debuffo"][0],estadisticas["debuffo"][1]}}
                    return nueva_arma
