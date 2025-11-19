"""
Simulador de mazmorra (Dungeon RPG) 🏰

Héroes (fuerza, magia, defensa, agilidad).

Monstruos (categorías: goblins, dragones, etc.).

Armas y pociones como ítems.

“Play” sería explorar habitaciones, encontrando enemigos aleatorios.

"""
import random
#--------------------DICCIONARIOS--------------------
clases = {
    1:"Guerrero",
    2:"Paladin",
    3:"Pícaro",
    4:"Cazador",
    5:"Mago",
    6:"Clerigo",
    7:"Druida",
    8:"Bardo",
    9:"Monje",
    10:"Nigromante"
}
#al subir de nivel se multiplican a todos los estadisticas entre 1,1 y 1,5
heroes = {
    1:{"nivel": 1,"nombre":"Guerrero","clase":1,"arma":"Escudo pesado","fuerza":6,"magia":1,"defensa":6,"agilidad":3,"vida": 13,"xp": 0},
    2:{"nivel": 1,"nombre":"Paladin","clase":2,"arma":"Espada larga","fuerza":4,"magia":4,"defensa":4,"agilidad":4,"vida": 12,"xp": 0},
    3:{"nivel": 1,"nombre":"Picaro","clase":3,"arma":"Dagas","fuerza":4,"magia":3,"defensa":2,"agilidad":7,"vida": 8,"xp": 0},
    4:{"nivel": 1,"nombre":"Cazador","clase":4,"arma":"Cuchillos de caza","fuerza":7,"magia":4,"defensa":3,"agilidad":5,"vida": 9,"xp": 0},
    5:{"nivel": 1,"nombre":"Mago","clase":5,"arma":"Baston Magico","fuerza":1,"magia":7,"defensa":3,"agilidad":2,"vida": 6,"xp": 0},
    6:{"nivel": 1,"nombre":"Clerigo","clase":6,"arma":"Stigma sagrado","fuerza":1,"magia":5,"defensa":5,"agilidad":3,"vida": 7,"xp": 0},
    7:{"nivel": 1,"nombre":"Druida","clase":7,"arma":"Totem","fuerza":3,"magia":5,"defensa":4,"agilidad":4,"vida": 10,"xp": 0},
    8:{"nivel": 1,"nombre":"Bardo","clase":8,"arma":"Laúd","fuerza":2,"magia":6,"defensa":5,"agilidad":3,"vida": 9,"xp": 0},
    9:{"nivel": 1,"nombre":"Monje","clase":9,"arma":"Nudilleras","fuerza":5,"magia":4,"defensa":2,"agilidad":4,"vida": 10,"xp": 0},
    10:{"nivel": 1,"nombre":"Nigromante","clase":10,"arma":"Baston oscuro","fuerza":1,"magia":8,"defensa":2,"agilidad":3,"vida": 7,"xp": 0}
}

armas = {
    1:{"clase":1,"nombre":"Escudo pesado","caracteristicas":{"fuerza":1,"defensa":6},"debuffo":{"agilidad":-2}},
    2:{"clase":2,"nombre":"Espada larga","caracteristicas":{"fuerza":4,"velocidad":2}},
    3:{"clase":3,"nombre":"Dagas","caracteristicas":{"fuerza":2,"agilidad":4}},
    4:{"clase":4,"nombre":"Cuchillos de caza","caracteristicas":{"fuerza":3,"agilidad":3}},
    5:{"clase":5,"nombre":"Baston Magico","caracteristicas":{"magia":5,"defensa":1}},
    6:{"clase":6,"nombre":"Stigma sagrado","caracteristicas":{"magia":4,"defensa":2},"debuffo":{"vida": -2}},
    7:{"clase":7,"nombre":"Totem","caracteristicas":{"fuerza":2,"defensa":4}},
    8:{"clase":8,"nombre":"Laúd","caracteristicas":{"defensa":2,"agilidad":4}},
    9:{"clase":9,"nombre":"Nudilleras","caracteristicas":{"fuerza":2,"magia":4}},
    10:{"clase":10,"nombre":"Baston oscuro","caracteristicas":{"magia":1,"defensa":5},"debuffo":{"vida": -3}}
}

#MONSTRUOS
monstruos_debiles = {
    #mountruos faciles de vencer
    1:{"nombre":"Rata Gigante","fuerza":5,"defensa":2,"vida":20},
    2:{"nombre":"Slime","fuerza":4,"defensa":3,"vida":25},
    3:{"nombre":"Goblin","fuerza":7,"defensa":2,"vida":30},
    4:{"nombre":"Esqueleto","fuerza":6,"defensa":3,"vida":35},
    5:{"nombre":"Esqueleto","fuerza":6,"defensa":3,"vida":35}
}

bestias = {
    1:{"nombre":"Lobo","fuerza":8,"defensa":3,"vida":40},
    2:{"nombre":"Oso","fuerza":12,"defensa":6,"vida":80},
    3:{"nombre":"Serpiente","fuerza":6,"defensa":2,"vida":35},
    4:{"nombre":"Jabali","fuerza":10,"defensa":5,"vida":60}
}

monstruos_enemigos_humanoides = {
    1:{"nombre":"Orco","fuerza":10,"defensa":4,"vida":50},
    2:{"nombre":"Trol","fuerza":12,"defensa":6,"vida":90},
    3:{"nombre":"Hombre lobo","fuerza":14,"defensa":4,"vida":70},
    4:{"nombre":"Bruja","fuerza":12,"defensa":3,"vida":60},
    5:{"nombre":"Nigromante enemigo","fuerza":10,"defensa":3,"vida":65}
}

monstruos_oscuros =  {
    1:{"nombre":"Ghoul","fuerza":6,"defensa":5,"vida":50},
    2:{"nombre":"Espectro","fuerza":10,"defensa":2,"vida":45},
    3:{"nombre":"Imp","fuerza":9,"defensa":3,"vida":35},
    4:{"nombre":"Gárgola","fuerza":15,"defensa":8,"vida":80}
}

criaturas_magicas = {
    1: {"nombre": "Dragón joven", "fuerza": 20, "defensa": 10, "vida": 150},
    2: {"nombre": "Quimera", "fuerza": 18, "defensa": 8, "vida": 120},
    3: {"nombre": "Mantícora", "fuerza": 22, "defensa": 9, "vida": 130},
    4: {"nombre": "Grifo", "fuerza": 20, "defensa": 10, "vida": 140},
    5: {"nombre": "Hidra", "fuerza": 25, "defensa": 12, "vida": 180}
}

monstruos_jefes = {
    1: {"nombre": "Rey goblin", "fuerza": 18, "defensa": 8, "vida": 100},
    2: {"nombre": "Señor de los muertos", "fuerza": 25, "defensa": 12, "vida": 200},
    3: {"nombre": "Golem", "fuerza": 30, "defensa": 20, "vida": 250},
    4: {"nombre": "Dragón anciano", "fuerza": 40, "defensa": 25, "vida": 500},
    5: {"nombre": "Señor demonio", "fuerza": 45, "defensa": 30, "vida": 600}
}

#--------------------MENUS--------------------
#--------------------Menu0 --------------------
menu0 = "Dragones y Mazmorras".center(40,"=") + "\n"+ \
    "1) Jugar" + "\n" +\
    "2) Crear" + "\n" +\
    "3) Editar" + "\n" +\
    "4) Listar" + "\n" +\
    "5) Salir" + "\n"

#--------------------Menu2--------------------
menu2 = "Menu de creacion".center(40,"=") + "\n"+ \
    "1) Crear personaje" + "\n" + \
    "2) Crear arma" + "\n" + \
    "3) Volver" + "\n"

nuevo_personaje = "Nuevo personaje".center(40,"=") + "\n"
cabezera_eleccion_clase = "Eleccion de clase".center(40,"=") + "\n"
eleccion_clase = ""
cabezera_eleccion_arma = "Eleccion de arma".center(40,"=") + "\n"
eleccion_arma = ""
eleccion_estadisticas = "Selecciona una estadistica".center(40,"=") + "\n" + \
    "1) Fuerza" + "\n" + \
    "2) Magia" + "\n" + \
    "3) Defensa" + "\n" + \
    "4) Agilidad" + "\n" + \
    "5) Vida" + "\n"
muestra_pers = "Personaje creado".center(40,"-") + "\n" \
    "Nombre: {}" + "\n" + \
    "Clase: {}" + "\n" + \
    "Arma: {}" + "\n" + \
    "estadisticas".center(40,"·") + "\n" \
    "Fuerza: {}" + "\n" + \
    "Magia: {}" + "\n" + \
    "Defensa: {}" + "\n" + \
    "Agilidad: {}" + "\n" + \
    "Vida: {}" + "\n"

nueva_arma = "Nueva arma".center(40,"=") + "\n"
eleccion_clase_arma = "Eleccion de clase de arma".center(40,"=") + "\n"
eleccion_estadisticas_arma = "Selecciona una estadistica".center(40,"=") + "\n" + \
    "1) Fuerza" + "\n" + \
    "2) Magia" + "\n" + \
    "3) Defensa" + "\n" + \
    "4) Agilidad" + "\n" + \
    "5) Vida" + "\n"
muestra_arma = "Arma creada".center(40,"=") + "\n" \
    "Nombre: {}" + "\n" + \
    "Requisito de clase: {}" + "\n" + \
    "Primera estadistica: {} = {}" + "\n" + \
    "Segunda estadistica: {} = {}" + "\n"

muestra_arma_deb = "Arma creada".center(40,"=") + "\n" \
    "Nombre: {}" + "\n" + \
    "Requisito de clase: {}" + "\n" + \
    "Primera estadistica: {} = {}" + "\n" + \
    "Segunda estadistica: {} = {}" + "\n" + \
    "Estadistica debuff: {} = {}" + "\n"

#--------------------Menu3--------------------
menu3 = "Menu de editar".center(40,"=") + "\n" + \
    "1) Editar personaje" + "\n" + \
    "2) Editar arma" + "\n" + \
    "3) Volver" + "\n"

menu_personaje = "Selecciona personaje".center(40,"=")

menu_arma = "Selecciona arma".center(40,"=")

pers_seleccion = "Editar {}".center(40,"=") + "\n" + \
    "1) Nombre" + "\n" + \
    "3) Cambiar arma" + "\n" + \
    "2) Salir" + "\n"

arma_seleccion = "Editar {}".center(40,"=") + "\n" + \
    "1) Nombre" + "\n" + \
    "2) Salir" + "\n"

#--------------------Menu4--------------------
menu4 = "Listas".center(40,"=") + "\n" + \
    "1) Lista personajes" + "\n" + \
    "2) Lista armas" + "\n" + \
    "3) Monstruos" + "\n" + \
    "4) Volver" + "\n"

menu41 = "\n" + " Lista personajes".center(40,"=") + "\n" +\
          "\n1)Listar por nivel\n2)Listar por nombre\n3)Listar por fuerza\n4)Listar por magia\n5)Listar por defensa\n6)Listar por agilidad"\
          "\n7)Listar por vida\n8)Listar por xp\n9)Go back"
menu042 = "Menu  042 (List Weapons)".center(50,"=")+"\n"\
          +"1)List by ID\n2)List by name\n3)List by Strength\n4)List by speed\n5)Go back"


#HAY QUE LISTAR POR PERSONAJES, ARMAS Y MONSTRUOS

listar_personajes = "Listar personajes".center(40,"=") + "\n" + \
    "1) Listar por ID" + "\n" + \
    "2) Listar por nombre" + "\n" + \
    "3) Listar por vida" + "\n" + \
    "4) Listar por XP" + "\n" + \
    "5) Listar por fuerza" + "\n" + \
    "6) Listar por defensa" + "\n" + \
    "7) Listar por agilidad" + "\n" + \
    "8) Listar por magia" + "\n" + \
    "9) Volver" + "\n"

listar_armas = "Listar armas".center(40,"=") + "\n" + \
    "1) Listar por ID" + "\n" + \
    "2) Listar por nombre" + "\n" + \
    "3) Listar por característica fuerza" + "\n" + \
    "4) Listar por característica magia" + "\n" + \
    "5) Listar por característica defensa" + "\n" + \
    "6) Listar por característica agilidad" + "\n" + \
    "7) Volver" + "\n"

menu_lista_monstruos = "Listas monstruos".center(40,"=") + "\n" + \
    "1) Monstruos debiles" + "\n" + \
    "2) Monstruos bestia" + "\n" + \
    "3) Monstruos humanoides" + "\n" + \
    "4) Monstruos oscuros" + "\n" + \
    "5) Criaturas magicas" + "\n" + \
    "6) Jefes" + "\n" + \
    "7) Volver" + "\n"

listar_debiles = "Monstruos debiles".center(40,"=") + "\n" + \
    "1) Por vida" + "\n" + \
    "2) Por ataque" + "\n" + \
    "3) Por defensa" + "\n" + \
    "4) Volver" + "\n"

listar_bestia = "Monstruos Bestia".center(40,"=") + "\n" + \
    "1) Por vida" + "\n" + \
    "2) Por ataque" + "\n" + \
    "3) Por defensa" + "\n" + \
    "4) Volver" + "\n"

listar_humanoides = "Monstruos humanoides".center(40,"=") + "\n" + \
    "1) Por vida" + "\n" + \
    "2) Por ataque" + "\n" + \
    "3) Por defensa" + "\n" + \
    "4) Volver" + "\n"

listar_oscuros = "Monstruos oscuros".center(40,"=") + "\n" + \
    "1) Por vida" + "\n" + \
    "2) Por ataque" + "\n" + \
    "3) Por defensa" + "\n" + \
    "4) Volver" + "\n"

listar_criaturas = "Criaturas magicas".center(40,"=") + "\n" + \
    "1) Por vida" + "\n" + \
    "2) Por ataque" + "\n" + \
    "3) Por defensa" + "\n" + \
    "4) Volver" + "\n"

listar_jefes = "Jefes".center(40,"=") + "\n" + \
    "1) Por vida" + "\n" + \
    "2) Por ataque" + "\n" + \
    "3) Por defensa" + "\n" + \
    "4) Volver" + "\n"

#PRINCIPAL
flg_salir = False
flg_menu0 = True

#CREAR
flg_menu2 = False
flg_crear_pers = False
flg_nombre = False
flg_clase = False
flg_arma = False
flg_estadisticas = False
flg_muestra = False

flg_crear_arma = False

#EDITAR
flg_menu3 = False
flg_edit_pers = False
flg_edit_arma = False

#LISTAR
flg_menu4 = False
flg_menu41 = False

opcion_invalida = "Opcion invalida"
fuera_rango = "Opcion fuera de rango"
formato_invalido = "Formato invalido."
arma_seleccionada = ""
encabezado_ranking_personajes = (
    "Ranking Personajes".center(106, "=") + "\n" +
    "Id".ljust(5) +
    "Nivel".ljust(10) +
    "Nombre".ljust(15) +
    "Clase".ljust(12) +
    "Arma".ljust(12) +
    "Fuerza".rjust(8) +
    "Magia".rjust(8) +
    "Defensa".rjust(10) +
    "Agilidad".rjust(10) +
    "Vida".rjust(8) +
    "Xp".rjust(8) + "\n" +
    "".center(106, "*")
)

while not flg_salir:
    while flg_menu0:
        print(menu0)
        opc = input("Opcion: \n")

        if not opc.isdigit():
            print(opcion_invalida)
            input("Enter para continuar")
        elif not int(opc) in range(1,6):
            print(fuera_rango)
            input("Enter para continuar")
        else:
            opc = int(opc)
            if opc == 1:
                print("Esta opcion de momento no esta implementada")
                input("Enter para continuar")
            elif opc == 2:
                flg_menu2 = True
                flg_menu0 = False
            elif opc == 3:
                flg_menu3 = True
                flg_menu0 = False
            elif opc == 4:
                flg_menu4 = True
                flg_menu0 = False
            else:
                flg_salir = True
                flg_menu0 = False
   
    # Crear
    while flg_menu2:
        print(menu2)
        opc = input("Opcion: \n")

        if not opc.isdigit():
            print(opcion_invalida)
            input("Enter para continuar")
        elif not int(opc) in range(1,4):
            print(fuera_rango)
            input("Enter para continuar")
        else:
            opc = int(opc)
            if opc == 1:
                flg_crear_pers = True
                flg_menu2 = False
            elif opc == 2:
                flg_crear_arma = True
                flg_menu2 = False   

            else:
                flg_menu0 = True
                flg_menu2 = False
  
    # Editar
    while flg_menu3:
        print(menu3)
        opc = input("Opcion: \n")

        if not opc.isdigit():
            print(opcion_invalida)
            input("Enter para continuar")
        elif not int(opc) in range(1,4):
            print(fuera_rango)
            input("Enter para continuar")
        else:
            opc = int(opc)
            if opc == 1:
                print("Esta opcion de momento no esta implementada")
                input("Enter para continuar")
            elif opc == 2:
                flg_edit_arma = True
                flg_menu3 = False
            else:
                flg_menu0 = True
                flg_menu3 = False
  
    #Listar
    while flg_menu4:
        print(menu4)
        opc = input("Opcion: \n")

        if not opc.isdigit():
            print(opcion_invalida)
            input("Enter para continuar")
        elif not int(opc) in range(1,5):
            print(fuera_rango)
            input("Enter para continuar")
        else:
            opc = int(opc)
            if opc == 1:
                flg_menu41 = True
                flg_menu4 = False
            elif opc == 2:
                print("Esta opcion de momento no esta implementada")
                input("Enter para continuar")
            elif opc == 3:
                print("Esta opcion de momento no esta implementada")
                input("Enter para continuar")
            else:
                flg_menu0 = True
                flg_menu4 = False
   
    # Listar personajes
    while flg_menu41:
        print(menu41)
        opc = input("Opcion: \n")
        if opc.isdigit():
            opc = int(opc)
            if opc in range(1,10):
                lista_ordenar = []
                for key in heroes:
                    lista_ordenar.append(key)
                if opc == 1:
                    for pasadas in range(len(lista_ordenar)):
                        cambios = False
                        for i in range(len(lista_ordenar) - 1 - pasadas):
                            if heroes[lista_ordenar[i]]["nivel"] > heroes[lista_ordenar[i + 1]]["nivel"]:
                                aux = lista_ordenar[i]
                                lista_ordenar[i] = lista_ordenar[i + 1]
                                lista_ordenar[i + 1] = aux
                                cambios = True
                        if not cambios:
                            break
                elif opc == 2:
                    for pasadas in range(len(lista_ordenar)):
                        cambios = False
                        for i in range(len(lista_ordenar) - 1 - pasadas):
                            if heroes[lista_ordenar[i]]["nombre"] > heroes[lista_ordenar[i + 1]]["nombre"]:
                                aux = lista_ordenar[i]
                                lista_ordenar[i] = lista_ordenar[i + 1]
                                lista_ordenar[i + 1] = aux
                                cambios = True
                        if not cambios:
                            break
                elif opc == 3:
                    for pasadas in range(len(lista_ordenar)):
                        cambios = False
                        for i in range(len(lista_ordenar) - 1 - pasadas):
                            if heroes[lista_ordenar[i]]["fuerza"] > heroes[lista_ordenar[i + 1]]["fuerza"]:
                                aux = lista_ordenar[i]
                                lista_ordenar[i] = lista_ordenar[i + 1]
                                lista_ordenar[i + 1] = aux
                                cambios = True
                        if not cambios:
                            break
                elif opc == 4:
                    for pasadas in range(len(lista_ordenar)):
                        cambios = False
                        for i in range(len(lista_ordenar) - 1 - pasadas):
                            if heroes[lista_ordenar[i]]["magia"] > heroes[lista_ordenar[i + 1]]["magia"]:
                                aux = lista_ordenar[i]
                                lista_ordenar[i] = lista_ordenar[i + 1]
                                lista_ordenar[i + 1] = aux
                                cambios = True
                        if not cambios:
                            break
                elif opc == 5:
                    for pasadas in range(len(lista_ordenar)):
                        cambios = False
                        for i in range(len(lista_ordenar) - 1 - pasadas):
                            if heroes[lista_ordenar[i]]["defensa"] > heroes[lista_ordenar[i + 1]]["defensa"]:
                                aux = lista_ordenar[i]
                                lista_ordenar[i] = lista_ordenar[i + 1]
                                lista_ordenar[i + 1] = aux
                                cambios = True
                        if not cambios:
                            break
                elif opc == 6:
                    for pasadas in range(len(lista_ordenar)):
                        cambios = False
                        for i in range(len(lista_ordenar) - 1 - pasadas):
                            if heroes[lista_ordenar[i]]["agilidad"] > heroes[lista_ordenar[i + 1]]["agilidad"]:
                                aux = lista_ordenar[i]
                                lista_ordenar[i] = lista_ordenar[i + 1]
                                lista_ordenar[i + 1] = aux
                                cambios = True
                        if not cambios:
                            break
                elif opc == 7:
                    for pasadas in range(len(lista_ordenar)):
                        cambios = False
                        for i in range(len(lista_ordenar) - 1 - pasadas):
                            if heroes[lista_ordenar[i]]["vida"] > heroes[lista_ordenar[i + 1]]["vida"]:
                                aux = lista_ordenar[i]
                                lista_ordenar[i] = lista_ordenar[i + 1]
                                lista_ordenar[i + 1] = aux
                                cambios = True
                        if not cambios:
                            break
                elif opc == 8:
                    for pasadas in range(len(lista_ordenar)):
                        cambios = False
                        for i in range(len(lista_ordenar) - 1 - pasadas):
                            if heroes[lista_ordenar[i]]["xp"] > heroes[lista_ordenar[i + 1]]["xp"]:
                                aux = lista_ordenar[i]
                                lista_ordenar[i] = lista_ordenar[i + 1]
                                lista_ordenar[i + 1] = aux
                                cambios = True
                        if not cambios:
                            break
                else:
                    flg_salir = True
                    flg_menu0 = False
                print(encabezado_ranking_personajes)
                for i in range(len(heroes)):
                    print(str(lista_ordenar[i]).ljust(5) +
                          str(heroes[lista_ordenar[i]]["nivel"]).ljust(10) + str(heroes[lista_ordenar[i]]["nombre"]).ljust(15) +
                          str(heroes[lista_ordenar[i]]["clase"]).ljust(12) + str( heroes[lista_ordenar[i]]["arma"]).ljust(12) +
                          str(heroes[lista_ordenar[i]]["fuerza"]).rjust(8) + str(heroes[lista_ordenar[i]]["magia"]).rjust(8) +
                          str(heroes[lista_ordenar[i]]["defensa"]).rjust(10) + str(heroes[lista_ordenar[i]]["agilidad"]).rjust(10) +
                          str(heroes[lista_ordenar[i]]["vida"]).rjust(8) + str(heroes[lista_ordenar[i]]["xp"]).rjust(8))
                input("Pulsa para continuar")
            else:
                print(fuera_rango)
                input("Enter para continuar")
        else:
            print(opcion_invalida)
            input("Enter para continuar")
    
    #Creacion de personaje
    while flg_crear_pers:
        nombre = ""
        clase = 0
        armas_disponible = []
        arma_personaje = 0
        estadistica_frz = 0
        estadistica_mag = 0
        estadistica_def = 0
        estadistica_agi = 0
        estadistica_vid = 0
        eleccion_clase = ""

        for i in range(len(clases)):
            if eleccion_clase == "":
                eleccion_clase = cabezera_eleccion_clase + "{}) ".format(i + 1) + clases[i + 1] + "\n"
            else:
                eleccion_clase = eleccion_clase + "{}) ".format(i + 1) + clases[i + 1] + "\n"
        flg_nombre = True

        while flg_nombre:
            print(nuevo_personaje)
            nombre = input("Nombre del personaje: ")

            if not nombre.isalpha():
                print(formato_invalido)
            else:
                print("Nuevo nombre creado {}".format(nombre))
                input("Enter para continuar")
                flg_clase = True
                flg_nombre = False

        while flg_clase:
            print(eleccion_clase)
            opc = input("Opcion:\n")
            if not opc.isdigit():
                print(opcion_invalida)
                input("Enter para continuar")

            elif int(opc) < 1 or int(opc) > len(clases):
                print(fuera_rango)
                input("Enter para continuar")
            else:
                opc = int(opc)
                print("Clase seleccionada {}".format(clases[opc]))
                input("Enter para continuar")
                clase = opc
                flg_arma = True
                flg_clase = False

        identificador = 0
        for i in range(len(armas)):
            if armas[i + 1]["clase"] == clase:
                identificador = identificador + 1
                if eleccion_arma == "":
                    eleccion_arma = cabezera_eleccion_arma + "{}) ".format(identificador) + armas[i + 1]["nombre"] + "\n"
                else:
                    eleccion_arma = eleccion_arma + "{}) ".format(identificador) + armas[i + 1]["nombre"] + "\n"
                armas_disponible.append(i + 1)

        while flg_arma:
            print(eleccion_arma)
            opc = input("Opcion:\n")
            if not opc.isdigit():
                print(formato_invalido)
            elif not int(opc) in range(1,len(armas_disponible) + 1) or int(opc) == 0:
                print(fuera_rango)
            else:
                opc = int(opc)
                print("Arma seleccionada {}.".format(armas[opc]["nombre"]))
                input("Enter para continuar")
                arma_personaje = opc
                estadistica_frz = 0
                estadistica_mag = 0
                estadistica_def = 0
                estadistica_agi = 0
                estadistica_vid = 0
                dado = 0
                flg_estadisticas = True
                flg_arma = False

        while flg_estadisticas:
            if estadistica_frz > 0 and estadistica_mag > 0 and estadistica_def > 0 and estadistica_agi > 0 and estadistica_vid > 0:
                print("\n"+"estadisticas Definitivos".center(40,"=") + "\nFuerza: {}\nMagia: {}\nDefensa: {}\nAgilidad: {}\nVida: {}\n".format(estadistica_frz,estadistica_mag,estadistica_def,estadistica_agi,estadistica_vid))
                input("Enter para continuar")
                flg_muestra = True
                flg_estadisticas = False
            else:
                print(eleccion_estadisticas)
                print("estadisticas Actuales".center(40,"=") + "\nFuerza: {} Magia: {} Defensa: {} Agilidad: {} Vida: {}\n".format(estadistica_frz, estadistica_mag, estadistica_def, estadistica_agi, estadistica_vid))
                opc = input("Opcion:\n")
                if not opc.isdigit():
                    print(opcion_invalida)
                    input("Enter para continuar")
                elif not int(opc) in range(1,6):
                    print(fuera_rango)
                    input("Enter para continuar")
                else:
                    opc = int(opc)
                    if opc == 1:
                        if estadistica_frz > 0:
                            print("No puedes cambiar el destino.")
                            input("Enter para continuar")
                        else:
                            dado = random.randint(10,20)
                            print("La fuerza sera de {} puntos.".format(dado))
                            input("Enter para continuar")
                            estadistica_frz = dado
                    elif opc == 2:
                        if estadistica_mag > 0:
                            print("No puedes cambiar el destino.")
                            input("Enter para continuar")
                        else:
                            dado = random.randint(10, 20)
                            print("La magia sera de {} puntos.".format(dado))
                            input("Enter para continuar")
                            estadistica_mag = dado
                    elif opc == 3:
                        if estadistica_def > 0:
                            print("No puedes cambiar el destino.")
                            input("Enter para continuar")
                        else:
                            dado = random.randint(10, 20)
                            print("La defensa sera de {} puntos.".format(dado))
                            input("Enter para continuar")
                            estadistica_def = dado
                    elif opc == 4:
                        if estadistica_agi > 0:
                            print("No puedes cambiar el destino.")
                            input("Enter para continuar")
                        else:
                            dado = random.randint(10, 20)
                            print("La agilidad sera de {} puntos.".format(dado))
                            input("Enter para continuar")
                            estadistica_agi = dado
                    else:
                        if estadistica_vid > 0:
                            print("No puedes cambiar el destino.")
                            input("Enter para continuar")
                        else:
                            dado = random.randint(10, 20)
                            print("La vida sera de {} puntos.".format(dado))
                            input("Enter para continuar")
                            estadistica_vid = dado

        while flg_muestra:
            print(muestra_pers.format(nombre, clases[clase], armas[arma_personaje]["nombre"], estadistica_frz, estadistica_mag, estadistica_def, estadistica_agi, estadistica_vid))
            opc = input("Quieres empezar la aventura? S/N\n")
            if opc != "S" and opc != "N":
                print("Tienes que poner una 'S' para aceptar o una 'N' para rechazar.")
                input("Enter para continuar")
            else:
                if opc == "N":
                    print("Mala suerte la proxima intenta jugar con lo que te salga.")
                    input("Enter para continuar")
                    flg_muestra = False
                else:
                    print("Personaje creado")
                    input("Enter para continuar")
                    heroes[len(heroes) + 1] = {"nivel":1, "nombre": nombre, "clase":clase, "arma" : armas[arma_personaje]["nombre"],
                                               "fuerza":estadistica_frz, "magia":estadistica_mag, "defensa":estadistica_def, "agilidad":estadistica_agi,
                                               "vida":estadistica_vid, "xp":0}
                    flg_muestra = False
        
        eleccion_clase = ""
        flg_menu0 = True
        flg_crear_pers = False

    #Creacion de arma 
    while flg_crear_arma:
        print(nueva_arma)
        clase = 0
        nombre_arma = ""
        nombre_estadistica1 = ""
        nombre_estadistica2 = ""
        estadistica1 = 0
        estadistica2 = 0
        nombre_debufo = ""
        debuff = 0
        
        for i in range(len(clases)):

            eleccion_clase_arma = eleccion_clase_arma + "{}) ".format(i + 1) + clases[i + 1] + "\n"
            if i + 1 == len(clases):
                break
       
        flg_clase = True  

        while flg_clase:
            print(eleccion_clase_arma)
            clase = input("Opcion:\n")
            if not clase.isdigit():
                print(opcion_invalida)
                input("Enter para continuar")
            elif not int(clase) in range(1,len(clases) + 1):
                print(fuera_rango)
                input("Enter para continuar")
            else:
                clase = int(clase)
                print("Requisito de {} para l'arma creado".format(clases[clase]))
                input("Enter para continuar")
                flg_clase = False
                flg_nombre = True
        
        while flg_nombre:
            nombre_arma = input("Nombre para l'arma:\n")
            probar_nombre = nombre_arma.replace(" ","")
            if not probar_nombre.isalpha():
                print(formato_invalido)
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
                flg_estadisticas = True
                flg_nombre = False
        

        contador_stats = 0
        while flg_estadisticas:
            if estadistica1 == 0 or estadistica2 == 0:
                print(eleccion_estadisticas_arma)
                opc = input("Opcion:\n")
                if not opc.isdigit():
                    print(formato_invalido)
                    input("Enter para continuar")
                elif not int(opc) in range(1,6):
                    print(fuera_rango)
                    input("Enter para continuar")
                else:
                    opc = int(opc)
                    if opc == 1 and contador_stats !=1:
                        if estadistica1 == 0:
                            nombre_estadistica1 = "fuerza"
                            estadistica1 = random.randint(1,6)
                            contador_stats = 1
                        else:
                            nombre_estadistica2 = "fuerza"
                            estadistica2 = random.randint(1,6)

                    elif opc == 2 and contador_stats != 2:
                        if estadistica1 == 0:
                            nombre_estadistica1 = "magia"
                            estadistica1 = random.randint(1,6)
                            contador_stats = 2
                        else:
                            nombre_estadistica2 = "magia"
                            estadistica2 = random.randint(1,6)
                    
                    elif opc == 3 and contador_stats != 3:
                        if estadistica1 == 0:
                            nombre_estadistica1 = "defensa"
                            estadistica1 = random.randint(1,6)
                            contador_stats = 3
                        else:
                            nombre_estadistica2 = "defensa"
                            estadistica2 = random.randint(1,6)
                        
                    elif opc == 4 and contador_stats != 4:
                        if estadistica1 == 0:
                            nombre_estadistica1 = "agilidad"
                            estadistica1 = random.randint(1,6)
                            contador_stats = 4
                        else:
                            nombre_estadistica2 = "agilidad"
                            estadistica2 = random.randint(1,6)
                    
                    elif opc == 5 and contador_stats != 5:
                        if estadistica1 == 0:
                            nombre_estadistica1 = "vida"
                            estadistica1 = random.randint(1,6)
                            contador_stats = 5
                        else:
                            nombre_estadistica2 = "vida"
                            estadistica2 = random.randint(1,6)
                    else:
                        print("Esta caracteristica ya la has elegido, elige otra.")
                        input("Enter para continuar")
            else:
                dec_deb = input("Quieres poner un debuff aleatorio? S/N \n(Si pones un debuff las estadistica tendran un aumento de un 50% en las estadisticas.\n" \
                "Pero el debuffo tembien sera de un aumento de 50%) ")
                if dec_deb == "S":
                    estadistica1 = int(estadistica1 * 1.5)
                    estadistica2 = int(estadistica2 * 1.5)
                    estadistica_random = random.randint(1,5)
                    flg_muestra = True
                    flg_estadisticas = False

                    if estadistica_random == 1:
                        nombre_debufo = "fuerza"
                        debuff = -int(random.randint(1,6) * 1.5)
                        flg_muestra = True
                        flg_estadisticas = False
                    
                    elif estadistica_random == 2:
                        nombre_debufo = "magia"
                        debuff = -int(random.randint(1,6) * 1.5)
                        flg_muestra = True
                        flg_estadisticas = False                   

                    elif estadistica_random == 3:
                        nombre_debufo = "defensa"
                        debuff = -int(random.randint(1,6) * 1.5)
                        flg_muestra = True
                        flg_estadisticas = False

                    elif estadistica_random == 4:
                        nombre_debufo = "agilidad"
                        debuff = -int(random.randint(1,6) * 1.5)
                        flg_muestra = True
                        flg_estadisticas = False

                    else:
                        nombre_debufo = "vida"
                        debuff = -int(random.randint(1,6) * 1.5)
                        flg_muestra = True
                        flg_estadisticas = False
                    
                    print("Las estadisticas del arma son:\n{} = {}\n{} = {}\n{} = {}".format(nombre_estadistica1, estadistica1, nombre_estadistica2, estadistica2, nombre_debufo, debuff))
                    input("Enter para continuar")
                    flg_muestra = True
                    flg_estadisticas = False

                elif dec_deb == "N":
                    print("Las estadisticas del arma son:\n{} = {}\n{} = {}\n".format(nombre_estadistica1, estadistica1, nombre_estadistica2, estadistica2))
                    input("Enter para continuar")
                    flg_muestra = True
                    flg_estadisticas = False

                else:
                    print(opcion_invalida)
                    input("Enter para continuar")
        
        while flg_muestra:
            if debuff == 0:
                print("Esta es la nueva arma:\n" + muestra_arma.format(nombre_arma, clases[clase], nombre_estadistica1, estadistica1, nombre_estadistica2, estadistica2))
            
            else:
                print("Esta es la nueva arma:\n" + muestra_arma_deb.format(nombre_arma, clases[clase], nombre_estadistica1, estadistica1, nombre_estadistica2, estadistica2, nombre_debufo, debuff))

            opc = input("Quieres crear esta arma? S/N\n")
            if opc != "S" and opc != "N":
                print("Tienes que poner una 'S' para aceptar o una 'N' para rechazar.")
                input("Enter para continuar")
            else:
                if opc == "N":
                    print("Mala suerte la proxima intenta jugar con lo que te salga.")
                    input("Enter para continuar")
                    flg_muestra = False
                else:
                    print("Arma guardada en el arsenal")
                    input("Enter para continuar")
                    print(debuff == 0)
                    if debuff == 0:
                        armas[len(armas) + 1] = {"clase" : clase, "nombre": nombre_arma,
                                               "caracteristicas":{nombre_estadistica1 : estadistica1, nombre_estadistica2 : estadistica2}}
                    else:
                        armas[len(armas) + 1] = {"clase" : clase, "nombre": nombre_arma,
                                               "caracteristicas":{nombre_estadistica1 : estadistica1, nombre_estadistica2 : estadistica2},
                                               "debuffo":{nombre_debufo:debuff}}
                                        
                    flg_muestra = False
        flg_menu0 = True
        flg_crear_arma = False
    
    #Editar armas
    while flg_edit_arma:
        eleccion_arma = ""
        for i in range(len(armas)):
            if eleccion_arma == "":
                eleccion_arma = cabezera_eleccion_arma + "{}) ".format(i + 1) + armas[i + 1]["nombre"] + "\n"
            else:
                eleccion_arma = eleccion_arma + "{}) ".format(i + 1) + armas[i + 1]["nombre"] + "\n"
        print(eleccion_arma)
        opc = input("Opcion:\n")
        if not opc.isdigit():
            print(formato_invalido)
            input("Enter para continuar")
        elif not int(opc) in range(1,len(armas) + 1):
            print(fuera_rango)
            input("Enter para continuar")
        else:
            
            opc = int(opc)
            nombre = armas[opc]["nombre"]

            print(arma_seleccion.format(nombre))
            opc_e = input("Opcion:\n")

            if not opc_e.isdigit():
                print(formato_invalido)
                input("Enter para continuar")
            elif not int(opc_e) in range(1,3):
                print(fuera_rango)
                input("Enter para continuar")
            else:
                

                opc_e = int(opc_e)
                if opc_e == 1:
                    nuevo_nombre = input("Nuevo nombre:\n")
                    if not nuevo_nombre.isalpha():
                            print(formato_invalido)
                            input("Enter to continue")
                    else:
                        print("El nombre: {}\nHa combiado por: {}".format(nombre,nuevo_nombre))
                        input("Enter para continuar")
                        armas[opc]["nombre"] = nuevo_nombre
                        flg_menu3 = True
                        flg_edit_arma = False
                else:
                    flg_menu3 = True
                    flg_edit_arma = False


