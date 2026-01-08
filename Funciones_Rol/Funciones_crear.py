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
            while flg_nombre:
            print(nuevo_personaje)
            nombre = input("Nombre del personaje: ")

            if not nombre.isalpha():
                print(formato_invalido_letras)
            else:
                print("Nuevo nombre creado {}".format(nombre))
                input("Enter para continuar")
                flg_clase = True
                flg_nombre = False

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
