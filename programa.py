import random
#--------------------HABILIDADES--------------------
#esto no se pondra en el documento
fuerza_total = 0
magia_total = 0
defensa_total = 0
agilidad_total = 0
vida_total = 0
defensa_total_mon = 0
fuerza_total_mon = 0
#formula para hacer efecto de perforacion daño_total - (defensa_total_mon - perforacion)
perforacion_basica = 0.1
perforacion_principal = 0.25
perforacion_ultimate = 0.6
habilidades = {
    "Guerrero":{"basico":{"nombre":"Golpe pesado","daño":fuerza_total},"principal":{"nombre":"Carga frontal","daño":fuerza_total*2,"retroceso":vida_total - (vida_total//5)},"ultimate":{"nombre":"Furia del titan","daño":fuerza_total,"buff":fuerza_total*1.5}},
    "Paladin":{"basico":{"nombre":"Espadazo sagrado","daño":fuerza_total + magia_total},"principal":{"nombre":"Castigo divino","daño":fuerza_total + magia_total,"debuffo":defensa_total_mon - (defensa_total_mon//3)},"ultimate":{"nombre":"Juicio celestial","daño":fuerza_total,"buff":vida_total + (vida_total//5)}},
    "Pícaro":{"basico":{"nombre":"Puñalada rápida","daño":fuerza_total*1.5},"principal":{"nombre":"Ataque furtivo","daño":fuerza_total*2},"ultimate":{"nombre":"Danza de sombras","daño":fuerza_total*3}},
    "Cazador":{"basico":{"nombre":"Flecha precisa","daño":fuerza_total - (defensa_total_mon - perforacion_basica)},"principal":{"nombre":"Disparo perforante","daño":fuerza_total - (defensa_total_mon - perforacion_basica)},"ultimate":{"nombre":"Furia del titan","daño":fuerza_total - (defensa_total_mon - perforacion_basica)}},
    "Mago":{"basico":{"nombre":"Bola mágica","daño":magia_total},"principal":{"nombre":"Explosión arcana","daño":magia_total*1.5},"ultimate":{"nombre":"Tormenta elemental","daño":magia_total*2}},
    "Clérigo":{"basico":{"nombre":"Luz purificadora","daño":magia_total,"buff":vida_total + (magia_total//3)},"principal":{"nombre":"Bendicion sagrada","buff":defensa_total * 2},"ultimate":{"nombre":"Milagro divino","buff":vida_total + (magia_total//3) + (vida_total//3)}},
    "Druida":{"basico":{"nombre":"Látigo de enredaderas","daño":magia_total + (fuerza_total)//5},"principal":{"nombre":"Forma bestial","buff":[fuerza_total * 1.5,agilidad_total * 1.5]},"ultimate":{"nombre":"Espiritu del bosque","buff":[magia_total*1.5,vida_total*1.5]}},
    "Bardo":{"basico":{"nombre":"Nota disonante","daño":magia_total},"principal":{"nombre":"Canción inspiradora","buff":[magia_total*1.5,agilidad_total*1.5]},"ultimate":{"nombre":"Sinfonía legendaria","debuffo":defensa_total_mon - (defensa_total_mon//5),"buff":[magia_total*1.5,defensa_total*1.5,agilidad_total*1.5]}},
    "Monje":{"basico":{"nombre":"Puño rapido","daño":fuerza_total + agilidad_total},"principal":{"nombre":"Combo devastador","daño":(fuerza_total*2)*3},"ultimate":{"nombre":"Técnica del dragón","daño":fuerza_total + defensa_total_mon}},
    "Nigromante":{"basico":{"nombre":"Toque oscuro","daño":magia_total},"principal":{"nombre":"Maldición de decadencia","daño":magia_total,"debuffo":[fuerza_total_mon - (fuerza_total_mon//3),defensa_total_mon - (defensa_total_mon//3)]},"ultimate":{"nombre":"Rito de aniquilación","daño":magia_total - (defensa_total_mon - 50)}}
}
#--------------------DICCIONARIOS--------------------
clases = {
    1:"Guerrero",
    2:"Paladin",
    3:"Pícaro",
    4:"Cazador",
    5:"Mago",
    6:"Clérigo",
    7:"Druida",
    8:"Bardo",
    9:"Monje",
    10:"Nigromante"
}
heroes = {
    1:{"nivel": 1,"nombre":"Manolo","clase":1,"arma":1,"fuerza":6,"magia":1,"defensa":6,"agilidad":3,"vida": 13,"xp": 0},
    2:{"nivel": 1,"nombre":"Antonia","clase":2,"arma":2,"fuerza":4,"magia":4,"defensa":4,"agilidad":4,"vida": 12,"xp": 0},
    3:{"nivel": 1,"nombre":"Antonio","clase":3,"arma":3,"fuerza":4,"magia":3,"defensa":2,"agilidad":7,"vida": 8,"xp": 0},
    4:{"nivel": 1,"nombre":"Zars","clase":4,"arma":4,"fuerza":7,"magia":4,"defensa":3,"agilidad":5,"vida": 9,"xp": 0},
    5:{"nivel": 1,"nombre":"Arca","clase":5,"arma":5,"fuerza":1,"magia":7,"defensa":3,"agilidad":2,"vida": 6,"xp": 0},
    6:{"nivel": 1,"nombre":"Moises","clase":6,"arma":6,"fuerza":1,"magia":5,"defensa":5,"agilidad":3,"vida": 7,"xp": 0},
    7:{"nivel": 1,"nombre":"Marc","clase":7,"arma":7,"fuerza":3,"magia":5,"defensa":4,"agilidad":4,"vida": 10,"xp": 0},
    8:{"nivel": 1,"nombre":"Ivan","clase":8,"arma":8,"fuerza":2,"magia":6,"defensa":5,"agilidad":3,"vida": 9,"xp": 0},
    9:{"nivel": 1,"nombre":"Ziah","clase":9,"arma":9,"fuerza":5,"magia":4,"defensa":2,"agilidad":4,"vida": 10,"xp": 0},
    10:{"nivel": 1,"nombre":"Teresa","clase":10,"arma":10,"fuerza":1,"magia":8,"defensa":2,"agilidad":3,"vida": 7,"xp": 0}
}
armas = {
    1:{"clase":1,"nombre":"Escudo Pesado","caracteristicas":{"fuerza":1,"defensa":6},"debuffo":{"agilidad":-2}},
    2:{"clase":2,"nombre":"Espada Larga","caracteristicas":{"fuerza":4,"agilidad":2}},
    3:{"clase":3,"nombre":"Dagas","caracteristicas":{"fuerza":2,"agilidad":4}},
    4:{"clase":4,"nombre":"Cuchillos de Caza","caracteristicas":{"fuerza":3,"agilidad":3}},
    5:{"clase":5,"nombre":"Baston Magico","caracteristicas":{"magia":5,"defensa":1}},
    6:{"clase":6,"nombre":"Stigma Sagrado","caracteristicas":{"magia":4,"defensa":2},"debuffo":{"vida": -2}},
    7:{"clase":7,"nombre":"Totem","caracteristicas":{"fuerza":2,"defensa":4}},
    8:{"clase":8,"nombre":"Laúd","caracteristicas":{"defensa":2,"agilidad":4}},
    9:{"clase":9,"nombre":"Nudilleras","caracteristicas":{"fuerza":2,"magia":4}},
    10:{"clase":10,"nombre":"Baston Oscuro","caracteristicas":{"magia":1,"defensa":5},"debuffo":{"vida": -3}}
}

#MONSTRUOS
monstruos_debiles = {
    #mountruos faciles de vencer
    1:{"nombre":"Rata Gigante","fuerza":5,"defensa":2,"vida":20,"xp_ganado":5},
    2:{"nombre":"Slime","fuerza":4,"defensa":3,"vida":25,"xp_ganado":8},
    3:{"nombre":"Goblin","fuerza":7,"defensa":2,"vida":30,"xp_ganado":12},
    4:{"nombre":"Esqueleto","fuerza":6,"defensa":3,"vida":35,"xp_ganado":10},
}

bestias = {
    1:{"nombre":"Lobo","fuerza":8,"defensa":3,"vida":40,"xp_ganado":15},
    2:{"nombre":"Oso","fuerza":12,"defensa":6,"vida":80,"xp_ganado":35},
    3:{"nombre":"Serpiente","fuerza":6,"defensa":2,"vida":35,"xp_ganado":20},
    4:{"nombre":"Jabali","fuerza":10,"defensa":5,"vida":60,"xp_ganado":18}
}

monstruos_enemigos_humanoides = {
    1:{"nombre":"Orco","fuerza":10,"defensa":4,"vida":50,"xp_ganado":30},
    2:{"nombre":"Trol","fuerza":12,"defensa":6,"vida":90,"xp_ganado":80},
    3:{"nombre":"Hombre lobo","fuerza":14,"defensa":4,"vida":70,"xp_ganado":50},
    4:{"nombre":"Bruja","fuerza":12,"defensa":3,"vida":60,"xp_ganado":40},
    5:{"nombre":"Nigromante enemigo","fuerza":10,"defensa":3,"vida":65,"xp_ganado":70}
}

monstruos_oscuros =  {
    1:{"nombre":"Ghoul","fuerza":6,"defensa":5,"vida":50,"xp_ganado":18},
    2:{"nombre":"Espectro","fuerza":10,"defensa":2,"vida":45,"xp_ganado":55},
    3:{"nombre":"Imp","fuerza":9,"defensa":3,"vida":35,"xp_ganado":60},
    4:{"nombre":"Gárgola","fuerza":15,"defensa":8,"vida":80,"xp_ganado":75}
}

criaturas_magicas = {
    1: {"nombre": "Dragón joven", "fuerza": 20, "defensa": 10, "vida": 150,"xp_ganado":300},
    2: {"nombre": "Quimera", "fuerza": 18, "defensa": 8, "vida": 120,"xp_ganado":180},
    3: {"nombre": "Mantícora", "fuerza": 22, "defensa": 9, "vida": 130,"xp_ganado":150},
    4: {"nombre": "Grifo", "fuerza": 20, "defensa": 10, "vida": 140,"xp_ganado":120},
    5: {"nombre": "Hidra", "fuerza": 25, "defensa": 12, "vida": 180,"xp_ganado":250}
}

monstruos_jefes = {
    1: {"nombre": "Rey goblin", "fuerza": 18, "defensa": 8, "vida": 100,"xp_ganado":200},
    2: {"nombre": "Señor de los muertos", "fuerza": 25, "defensa": 12, "vida": 200,"xp_ganado":450},
    3: {"nombre": "Golem", "fuerza": 30, "defensa": 20, "vida": 250,"xp_ganado":5,"xp_ganado":350},
    4: {"nombre": "Dragón anciano", "fuerza": 40, "defensa": 25, "vida": 500,"xp_ganado":800},
    5: {"nombre": "Señor demonio", "fuerza": 45, "defensa": 30, "vida": 600,"xp_ganado":1200}
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
    "Nivel: {}" + "\n" + \
    "Arma: {}" + "\n" + \
    "Estadisticas".center(40,"·") + "\n" \
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

menu_personaje = "Selecciona personaje".center(40,"=") + "\n"

menu_arma = "Selecciona arma".center(40,"=") + "\n"

arma_seleccion = "Editar {}".center(40,"=") + "\n" + \
    "1) Nombre" + "\n" + \
    "2) Característica 1" + "\n" + \
    "3) Característica 2" + "\n" + \
    "4) Salir" + "\n"
pers_seleccion = "Editar {}".center(40,"=") + "\n" + \
    "1) Nombre" + "\n" + \
    "2) Cambiar arma" + "\n" + \
    "3) Salir" + "\n"

arma_seleccion = "Editar {}".center(40,"=") + "\n" + \
    "1) Nombre" + "\n" + \
    "2) Salir" + "\n"

#--------------------Menu4--------------------
menu4 = "Listas".center(40,"=") + "\n" + \
    "1) Lista personajes" + "\n" + \
    "2) Lista armas" + "\n" + \
    "3) Monstruos" + "\n" + \
    "4) Volver" + "\n"




#HAY QUE LISTAR POR PERSONAJES, ARMAS Y MONSTRUOS

menu41 = "\n" + " Lista personajes".center(40,"=") + "\n" +\
          "\n1)Listar por nivel\n2)Listar por nombre\n3)Listar por fuerza\n4)Listar por magia\n5)Listar por defensa\n6)Listar por agilidad"\
          "\n7)Listar por vida\n8)Listar por xp\n9)Go back"
menu042 = "Menu  042 (List Weapons)".center(50,"=")+"\n"\
          +"1)List by ID\n2)List by name\n3)List by Strength\n4)List by speed\n5)Go back"

listar_personajes = "Listar personajes".center(40,"=") + "\n" + \
    "1) Listar por ID" + "\n" + \
    "2) Listar por nombre" + "\n" + \
    "3) Listar por fuerza" + "\n" + \
    "4) Listar por magia" + "\n" + \
    "5) Listar por defensa" + "\n" + \
    "6) Listar por agilidad" + "\n" + \
    "7) Listar por vida" + "\n" + \
    "8) Volver" + "\n"

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

empezar_a_jugar = "Selecciona un heroe".center(50,"*") + "\n"


#PRINCIPAL
flg_salir = False
flg_menu0 = True
flg_jugar = False

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
flg_nivel = False
flg_edit_pers = False
flg_edit_arma = False

#LISTAR
flg_menu4 = False
flg_menu41 = False
flg_menu42 = False
flg_menu43 = False
nombre = ""
opc2 = ""
lista_ordenar = []

fuera_rango = "Opcion fuera de rango"
formato_invalido_letras = "Formato invalido tienen que ser letras."
formato_invalido_numeros = "Formato invalido tienen que ser numeros."
arma_seleccionada = ""
encabezado_ranking_personajes = (
        "Ranking Personajes".center(123, "=") + "\n" +
        "Id".ljust(5) +
        "Nivel".ljust(10) +
        "Nombre".ljust(20) +
        "Clase".ljust(20) +
        "Arma".ljust(21) +
        "Fuerza".ljust(8) +
        "Magia".ljust(8) +
        "Defensa".ljust(10) +
        "Agilidad".ljust(10) +
        "Vida".ljust(8) +
        "Xp".ljust(8) + "\n" +
        "".center(123, "*")
)
encabezado_ranking_armas = (
    "Ranking Armas".center(106, "=") + "\n" +
    "Id".ljust(5) +
    "Nombre".ljust(15)
)

while not flg_salir:
    while flg_menu0:
        print(menu0)
        opc = input("Opcion: \n")

        if not opc.isdigit():
            print(formato_invalido_numeros)
            input("Enter para continuar")
        elif not int(opc) in range(1,6):
            print(fuera_rango)
            input("Enter para continuar")
        else:
            opc = int(opc)
            if opc == 1:
                flg_jugar = True
                flg_menu0 = False
                contador = 0
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
    
    #Juego
    while flg_jugar:
        monstruo = ""
        if contador < 10:
            monstruo = monstruos_debiles[random.randint(1,4)]
        else:
            monstruo = bestias[random.randint(1,4)]
        print(contador,monstruo)
        input()
        contador = contador + 1
        #cada 10 pisos aumenta que enemigos puedes aparecer
        #la barra de xp cada vez que se sube de nivel aumente un 1.5

    # Elegir que crear
    while flg_menu2:
        print(menu2)
        opc = input("Opcion: \n")

        if not opc.isdigit():
            print(formato_invalido_numeros)
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
            print(formato_invalido_numeros)
            input("Enter para continuar")
        elif not int(opc) in range(1,4):
            print(fuera_rango)
            input("Enter para continuar")
        else:
            opc = int(opc)
            if opc == 1:
                flg_edit_pers = True
                flg_menu3 = False
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
            print(formato_invalido_numeros)
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
                flg_menu42 = True
                flg_menu4 = False
            elif opc == 3:
                flg_menu43 = True
                flg_menu4 = False
            else:
                flg_menu0 = True
                flg_menu4 = False
    
    # Listar personajes
    while flg_menu41:
        print(listar_personajes)
        opc = input("Opcion: \n")
        if opc.isdigit():
            opc = int(opc)
            if opc in range(1,9):
                lista_ordenar = []
                for key in heroes:
                    lista_ordenar.append(key)
                if opc == 1:
                    for pasadas in range(len(lista_ordenar)):
                        cambios = False
                        for i in range(len(lista_ordenar) - 1 - pasadas):
                            if lista_ordenar[i] > lista_ordenar[i+1]:
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
                            if heroes[lista_ordenar[i]]["fuerza"] < heroes[lista_ordenar[i + 1]]["fuerza"]:
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
                            if heroes[lista_ordenar[i]]["magia"] < heroes[lista_ordenar[i + 1]]["magia"]:
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
                            if heroes[lista_ordenar[i]]["defensa"] < heroes[lista_ordenar[i + 1]]["defensa"]:
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
                            if heroes[lista_ordenar[i]]["agilidad"] < heroes[lista_ordenar[i + 1]]["agilidad"]:
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
                            if heroes[lista_ordenar[i]]["vida"] < heroes[lista_ordenar[i + 1]]["vida"]:
                                aux = lista_ordenar[i]
                                lista_ordenar[i] = lista_ordenar[i + 1]
                                lista_ordenar[i + 1] = aux
                                cambios = True
                        if not cambios:
                            break
                else:
                    flg_menu41 = False
                    flg_menu4 = True
                    break
                if flg_menu41:
                    print(encabezado_ranking_personajes)

                    for hero_id in lista_ordenar:
                        # [fuerza, defensa, agilidad, vida, magia]
                        stats_bonos = [0, 0, 0, 0, 0]

                        id_arma = heroes[hero_id]["arma"]

                        caracts = armas[id_arma].get("caracteristicas", {})
                        stats_bonos[0] += caracts.get("fuerza", 0)
                        stats_bonos[1] += caracts.get("defensa", 0)
                        stats_bonos[2] += caracts.get("agilidad", 0)
                        stats_bonos[3] += caracts.get("vida", 0)
                        stats_bonos[4] += caracts.get("magia", 0)

                        debuffos = armas[id_arma].get("debuffo", {})
                        stats_bonos[0] += debuffos.get("fuerza", 0)
                        stats_bonos[1] += debuffos.get("defensa", 0)
                        stats_bonos[2] += debuffos.get("agilidad", 0)
                        stats_bonos[3] += debuffos.get("vida", 0)
                        stats_bonos[4] += debuffos.get("magia", 0)
                        print(str(hero_id).ljust(5) +
                              str(heroes[hero_id]["nivel"]).ljust(10) +
                              str(heroes[hero_id]["nombre"]).ljust(20) +
                              str(clases[heroes[hero_id]["clase"]]).ljust(20) +
                              str(armas[id_arma]["nombre"]).ljust(21) +
                              str(heroes[hero_id]["fuerza"] + stats_bonos[0]).ljust(8) +
                              str(heroes[hero_id]["magia"] + stats_bonos[4]).ljust(8) +
                              str(heroes[hero_id]["defensa"] + stats_bonos[1]).ljust(10) +
                              str(heroes[hero_id]["agilidad"] + stats_bonos[2]).ljust(10) +
                              str(heroes[hero_id]["vida"] + stats_bonos[3]).ljust(8) +
                              str(heroes[hero_id]["xp"]).ljust(8))
                    print("".center(123, "="))
                    input("Pulsa para continuar")
            else:
                print(fuera_rango)
                input("Enter para continuar")
        else:
            print(formato_invalido_numeros)
            input("Enter para continuar")
    
    # Listar armas
    while flg_menu42:
        print(listar_armas)
        opc_input = input("Opcion :")

        if not opc_input.isdigit():
            print("Opcion no numerica:")
            input("Enter to Continue")
        elif not int(opc_input) in range(1, 8):
            print("Opcion numerica fuera de rango")
            input("Enter to Continue")
        else:
            opc = int(opc_input)
            lista_ordenar = []
            propiedad_ordenar = ""

            for key in armas:
                lista_ordenar.append(key)


            if opc == 1:
                propiedad_ordenar = "ID"
                for pasadas in range(len(lista_ordenar)):
                    cambios = False
                    for i in range(len(lista_ordenar) - 1 - pasadas):
                        if lista_ordenar[i] > lista_ordenar[i + 1]:
                            aux = lista_ordenar[i]
                            lista_ordenar[i] = lista_ordenar[i + 1]
                            lista_ordenar[i + 1] = aux
                            cambios = True
                    if not cambios:
                        break

            elif opc == 2:
                propiedad_ordenar = "nombre"
                for pasadas in range(len(lista_ordenar)):
                    cambios = False
                    for i in range(len(lista_ordenar) - 1 - pasadas):
                        if armas[lista_ordenar[i]]["nombre"]> armas[lista_ordenar[i+1]]["nombre"]:
                            aux = lista_ordenar[i]
                            lista_ordenar[i] = lista_ordenar[i + 1]
                            lista_ordenar[i + 1] = aux
                            cambios = True
                    if not cambios:
                        break

            elif opc == 3:
                propiedad_ordenar = "fuerza"

                lista_filtrada = []
                for key in lista_ordenar:
                    if propiedad_ordenar in armas[key].get("caracteristicas", {}) or \
                            propiedad_ordenar in armas[key].get("debuffo", {}):
                        lista_filtrada.append(key)
                lista_ordenar = lista_filtrada


                if lista_ordenar:
                    for pasadas in range(len(lista_ordenar)):
                        cambios = False
                        for i in range(len(lista_ordenar) - 1 - pasadas):
                            # Obtener el valor, priorizando el debuffo si existe, si no la característica
                            valor1 = armas[lista_ordenar[i]].get("debuffo", {}).get(propiedad_ordenar,
                                                                                    armas[lista_ordenar[i]].get(
                                                                                        "caracteristicas", {}).get(
                                                                                        propiedad_ordenar, 0))
                            valor2 = armas[lista_ordenar[i + 1]].get("debuffo", {}).get(propiedad_ordenar,
                                                                                        armas[lista_ordenar[i + 1]].get(
                                                                                            "caracteristicas", {}).get(
                                                                                            propiedad_ordenar, 0))

                            if valor1 < valor2:
                                aux = lista_ordenar[i]
                                lista_ordenar[i] = lista_ordenar[i + 1]
                                lista_ordenar[i + 1] = aux
                                cambios = True
                        if not cambios:
                            break

            elif opc == 4:
                propiedad_ordenar = "magia"

                lista_filtrada = []
                for key in lista_ordenar:
                    if propiedad_ordenar in armas[key].get("caracteristicas", {}) or \
                            propiedad_ordenar in armas[key].get("debuffo", {}):
                        lista_filtrada.append(key)
                lista_ordenar = lista_filtrada

                if lista_ordenar:
                    for pasadas in range(len(lista_ordenar)):
                        cambios = False
                        for i in range(len(lista_ordenar) - 1 - pasadas):
                            valor1 = armas[lista_ordenar[i]].get("debuffo", {}).get(propiedad_ordenar,
                                                                                    armas[lista_ordenar[i]].get(
                                                                                        "caracteristicas", {}).get(
                                                                                        propiedad_ordenar, 0))
                            valor2 = armas[lista_ordenar[i + 1]].get("debuffo", {}).get(propiedad_ordenar,
                                                                                        armas[lista_ordenar[i + 1]].get(
                                                                                            "caracteristicas", {}).get(
                                                                                            propiedad_ordenar, 0))

                            if valor1 < valor2:
                                aux = lista_ordenar[i]
                                lista_ordenar[i] = lista_ordenar[i + 1]
                                lista_ordenar[i + 1] = aux
                                cambios = True
                        if not cambios:
                            break

            elif opc == 5:
                propiedad_ordenar = "defensa"

                # FILTRADO
                lista_filtrada = []
                for key in lista_ordenar:
                    if propiedad_ordenar in armas[key].get("caracteristicas", {}) or \
                            propiedad_ordenar in armas[key].get("debuffo", {}):
                        lista_filtrada.append(key)
                lista_ordenar = lista_filtrada


                if lista_ordenar:
                    for pasadas in range(len(lista_ordenar)):
                        cambios = False
                        for i in range(len(lista_ordenar) - 1 - pasadas):
                            valor1 = armas[lista_ordenar[i]].get("debuffo", {}).get(propiedad_ordenar,
                                                                                    armas[lista_ordenar[i]].get(
                                                                                        "caracteristicas", {}).get(
                                                                                        propiedad_ordenar, 0))
                            valor2 = armas[lista_ordenar[i + 1]].get("debuffo", {}).get(propiedad_ordenar,
                                                                                        armas[lista_ordenar[i + 1]].get(
                                                                                            "caracteristicas", {}).get(
                                                                                            propiedad_ordenar, 0))

                            if valor1 < valor2:
                                aux = lista_ordenar[i]
                                lista_ordenar[i] = lista_ordenar[i + 1]
                                lista_ordenar[i + 1] = aux
                                cambios = True
                        if not cambios:
                            break

            elif opc == 6:
                propiedad_ordenar = "agilidad"

                lista_filtrada = []
                for key in lista_ordenar:
                    if propiedad_ordenar in armas[key].get("caracteristicas", {}) or \
                            propiedad_ordenar in armas[key].get("debuffo", {}):
                        lista_filtrada.append(key)
                lista_ordenar = lista_filtrada


                if lista_ordenar:
                    for pasadas in range(len(lista_ordenar)):
                        cambios = False
                        for i in range(len(lista_ordenar) - 1 - pasadas):
                            valor1 = armas[lista_ordenar[i]].get("debuffo", {}).get(propiedad_ordenar,
                                                                                    armas[lista_ordenar[i]].get(
                                                                                        "caracteristicas", {}).get(
                                                                                        propiedad_ordenar, 0))
                            valor2 = armas[lista_ordenar[i + 1]].get("debuffo", {}).get(propiedad_ordenar,
                                                                                        armas[lista_ordenar[i + 1]].get(
                                                                                            "caracteristicas", {}).get(
                                                                                            propiedad_ordenar, 0))

                            if valor1 < valor2:
                                aux = lista_ordenar[i]
                                lista_ordenar[i] = lista_ordenar[i + 1]
                                lista_ordenar[i + 1] = aux
                                cambios = True
                        if not cambios:
                            break

            elif opc == 7:
                flg_menu4 = True
                flg_menu42 = False

            if flg_menu42 and lista_ordenar:

                encabezado_ranking_armas = (
                        f"Ranking Armas por {propiedad_ordenar.capitalize()}".center(80, "=") + "\n" +
                        "ID".ljust(5) +
                        "Nombre".ljust(20) +
                        "Clase".ljust(10) +
                        "Fuerza".ljust(10) +
                        "Magia".ljust(10) +
                        "Defensa".ljust(10) +
                        "Agilidad".ljust(10) +
                        "Vida".ljust(10) +
                        "\n" + "".center(80, "*")
                )
                print(encabezado_ranking_armas)
                for key in lista_ordenar:
                    arma = armas[key]
                    caract = arma.get("caracteristicas", {})
                    debuffo = arma.get("debuffo", {})

                    fuerza_base = caract.get("fuerza", 0)
                    magia_base = caract.get("magia", 0)
                    defensa_base = caract.get("defensa", 0)
                    agilidad_base = caract.get("agilidad", 0)

                    fuerza_debuffo = debuffo.get("fuerza", 0)
                    magia_debuffo = debuffo.get("magia", 0)
                    defensa_debuffo = debuffo.get("defensa", 0)
                    agilidad_debuffo = debuffo.get("agilidad", 0)
                    vida_debuffo = debuffo.get("vida", 0)


                    fuerza_efectiva = fuerza_base + fuerza_debuffo
                    if fuerza_base != 0 or fuerza_debuffo != 0:
                        fuerza_val = str(fuerza_efectiva)
                    else:
                        fuerza_val = "-"

                    magia_efectiva = magia_base + magia_debuffo
                    if magia_base != 0 or magia_debuffo != 0:
                        magia_val = str(magia_efectiva)
                    else:
                        magia_val = "-"

                    # DEFENSA
                    defensa_efectiva = defensa_base + defensa_debuffo
                    if defensa_base != 0 or defensa_debuffo != 0:
                        defensa_val = str(defensa_efectiva)
                    else:
                        defensa_val = "-"

                    agilidad_efectiva = agilidad_base + agilidad_debuffo
                    if agilidad_base != 0 or agilidad_debuffo != 0:
                        agilidad_val = str(agilidad_efectiva)
                    else:
                        agilidad_val = "-"

                    if vida_debuffo != 0:
                        vida_val = str(vida_debuffo)
                    else:
                        vida_val = "-"


                    print(str(key).ljust(5) +
                          arma.get("nombre", "N/A").ljust(20) +
                          str(arma.get("clase", "-")).ljust(10) +
                          fuerza_val.ljust(10) +
                          magia_val.ljust(10) +
                          defensa_val.ljust(10) +
                          agilidad_val.ljust(10) +
                          vida_val.ljust(10))

                print("".center(80, "="))
                input("Pulsa para continuar")
    
    # Listar Monstruos
    while flg_menu43:
        print(menu_lista_monstruos)
        opc = input("Opcion :")
        if not opc.isdigit():
            print("Opcion no numerica:")
            input("Enter to Continue")
        elif not int(opc) in range(1, 8):
            print("Opcion numerica fuera de rango")
            input("Enter to Continue")
        else:
            opc = int(opc)
            if opc == 1:
                nombre= "Monstruos Debiles"
                opc2 = monstruos_debiles
                lista_ordenar = []
                for key in monstruos_debiles:
                    lista_ordenar.append(key)
            elif opc == 2:
                nombre= "Bestias "
                opc2 = bestias
                lista_ordenar = []
                for key in bestias:
                    lista_ordenar.append(key)
            elif opc == 3:
                nombre= "Monstruo Enemigos Humanoides "
                opc2 = monstruos_enemigos_humanoides
                lista_ordenar = []
                for key in monstruos_enemigos_humanoides:
                    lista_ordenar.append(key)
            elif opc == 4:
                nombre = "Monstruos Oscuros"
                opc2 = monstruos_oscuros
                lista_ordenar = []
                for key in monstruos_oscuros:
                    lista_ordenar.append(key)
            elif opc == 5:
                nombre = "Criaturas Magicas"
                opc2 = criaturas_magicas
                lista_ordenar = []
                for key in criaturas_magicas:
                    lista_ordenar.append(key)
            elif opc == 6:
                nombre = "Jefes"
                opc2 = monstruos_jefes
                lista_ordenar = []
                for key in monstruos_jefes:
                    lista_ordenar.append(key)
            else:
                flg_menu4 = True
                flg_menu43 = False
            listar_mostruos = "{}".format(nombre).center(40, "=") + "\n" + \
                           "1) Por vida" + "\n" + \
                           "2) Por ataque" + "\n" + \
                           "3) Por defensa" + "\n" + \
                           "4) Volver" + "\n"
            print(listar_mostruos)
            opc = input("Opcion :")
            if not opc.isdigit():
                print("Opcion no numerica:")
                input("Enter to Continue")
            elif not int(opc) in range(1, 5):
                print("Opcion numerica fuera de rango")
                input("Enter to Continue")
            else:
                opc = int(opc)
                if opc == 1:
                    for pasadas in range(len(lista_ordenar)):
                        cambios = False
                        for i in range(len(lista_ordenar) - 1 - pasadas):
                            if opc2[lista_ordenar[i]]["vida"] < opc2[lista_ordenar[i + 1]]["vida"]:
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
                            if opc2[lista_ordenar[i]]["fuerza"] < opc2[lista_ordenar[i + 1]]["fuerza"]:
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
                            if opc2[lista_ordenar[i]]["defensa"] < opc2[lista_ordenar[i + 1]]["defensa"]:
                                aux = lista_ordenar[i]
                                lista_ordenar[i] = lista_ordenar[i + 1]
                                lista_ordenar[i + 1] = aux
                                cambios = True
                        if not cambios:
                            break
                else:
                    flg_menu4 = True
                    flg_menu42 = False
                if flg_menu43 :
                    encabezado_ranking_monstruos= (
                            ("Ranking "+nombre).center(50, "=") + "\n" +
                            "Id".ljust(5) +
                            "Nombre".ljust(25) +
                            "Fuerza".ljust(8) +
                            "Defensa".ljust(8) +
                            "Vida".ljust(8))
                    print(encabezado_ranking_monstruos)
                    for i in range(len(opc2)):
                        print(str(lista_ordenar[i]).ljust(5) +
                              str(opc2[lista_ordenar[i]]["nombre"]).ljust(25) +
                              str(opc2[lista_ordenar[i]]["fuerza"]).ljust(8) +
                              str(opc2[lista_ordenar[i]]["defensa"]).ljust(8) +
                              str(opc2[lista_ordenar[i]]["vida"]).ljust(8))
                    print("".center(50,"="))
    
    #Creacion de personaje
    while flg_crear_pers:
        nombre = ""
        clase = 0
        nivel = 0
        armas_disponible = []
        arma_personaje = 0
        estadistica_frz = 0
        estadistica_mag = 0
        estadistica_def = 0
        estadistica_agi = 0
        estadistica_vid = 0
        eleccion_clase = ""
        eleccion_arma = ""

        flg_nombre = True

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
        
        #ordenar clases
        keys_clases = list(clases.keys())
        for pasada in range(len(keys_clases)):
            cambios = False
            for i in range(len(keys_clases)-1-pasada):
                if clases[keys_clases[i]] > clases[keys_clases[i+1]]:
                    cambios = True
                    aux = keys_clases[i]
                    keys_clases[i] = keys_clases[i+1]
                    keys_clases[i+1] = aux
            if not cambios:
                break
        
        for i in range(len(keys_clases)):
            eleccion_clase = eleccion_clase + "{}) ".format(i + 1) + clases[keys_clases[i]] + "\n"

        while flg_clase:
            print(cabezera_eleccion_clase + eleccion_clase)
            opc = input("Opcion:\n")
            if not opc.isdigit():
                print(formato_invalido_numeros)
                input("Enter para continuar")

            elif int(opc) < 1 or int(opc) > len(clases):
                print(fuera_rango)
                input("Enter para continuar")
            else:
                opc = int(opc)
                print("Clase seleccionada {}".format(clases[keys_clases[opc-1]]))
                input("Enter para continuar")
                clase = keys_clases[opc-1]
                flg_nivel = True
                flg_clase = False

        while flg_nivel:
            new_nivel = input("Con que nivel quieres empezar la aventura? (1 - 5)\n")
            if not new_nivel.isdigit():
                print(formato_invalido_numeros)
            elif not int(new_nivel) in range(1,6):
                print("El nivel solo puede estar entre 1 y 5")
            else:
                nivel = int(new_nivel)
                flg_arma = True
                flg_nivel = False
        
        #ordenar armas
        keys_arma = list(armas.keys())
        for pasada in range(len(keys_arma)):
            cambios = False
            for i in range(len(keys_arma)-1-pasada):
                if armas[keys_arma[i]]["nombre"] > armas[keys_arma[i+1]]["nombre"]:
                    cambios = True
                    aux = keys_arma[i]
                    keys_arma[i] = keys_arma[i+1]
                    keys_arma[i + 1] = aux
            if not cambios:
                break

        for id in keys_arma:
            if armas[id]["clase"] == clase:
                armas_disponible.append(id)
                eleccion_arma = eleccion_arma + "{}) ".format(len(armas_disponible)) + armas[id]["nombre"] + "\n"

        while flg_arma:
            print(cabezera_eleccion_arma + eleccion_arma)
            opc = input("Opcion:\n")
            if not opc.isdigit():
                print(formato_invalido_numeros)
            elif not int(opc) in range(1,len(armas_disponible) + 1):
                print(fuera_rango)
            else:
                opc = int(opc)
                print("Arma seleccionada {}.".format(armas[armas_disponible[opc-1]]["nombre"]))
                input("Enter para continuar")
                arma_personaje = armas_disponible[opc-1]
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
                print("\n"+"estadisticas Definitivos".center(40,"=") + "\nFuerza: {}\nMagia: {}\nDefensa: {}\nAgilidad: {}\nVida: {}\nCuenta que al subir de nivel sube entre un 3% - 12%".format(estadistica_frz,estadistica_mag,estadistica_def,estadistica_agi,estadistica_vid))
                input("Enter para continuar")
                flg_muestra = True
                flg_estadisticas = False
            else:
                print(eleccion_estadisticas)
                print("estadisticas Actuales".center(40,"=") + "\nFuerza: {} Magia: {} Defensa: {} Agilidad: {} Vida: {}\n".format(estadistica_frz, estadistica_mag, estadistica_def, estadistica_agi, estadistica_vid))
                opc = input("Opcion:\n")
                if not opc.isdigit():
                    print(formato_invalido_numeros)
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
            if nivel > 1:
                for i in range(nivel):
                    estadistica_frz = estadistica_frz * (1.0 + (random.randrange(30,140))/1000)
                    estadistica_mag = estadistica_mag * (1.0 + (random.randrange(30,140))/1000)
                    estadistica_def = estadistica_def * (1.0 + (random.randrange(30,140))/1000)
                    estadistica_agi = estadistica_agi * (1.0 + (random.randrange(30,140))/1000)
                    estadistica_vid = estadistica_vid * (1.0 + (random.randrange(30,140))/1000)
            
            estadistica_frz = int(estadistica_frz)
            estadistica_mag = int(estadistica_mag)
            estadistica_def = int(estadistica_def)
            estadistica_agi = int(estadistica_agi)
            estadistica_vid = int(estadistica_vid)

            print(muestra_pers.format(nombre, clases[clase],nivel, armas[arma_personaje]["nombre"], estadistica_frz, estadistica_mag, estadistica_def, estadistica_agi, estadistica_vid))
            opc = input("Quieres empezar la aventura? S/N\n")
            if opc.upper() != "S" and opc.upper() != "N":
                print("Tienes que poner una 'S' para aceptar o una 'N' para rechazar.")
                input("Enter para continuar")
            else:
                if opc.upper() == "N":
                    print("Mala suerte la proxima intenta jugar con lo que te salga.")
                    input("Enter para continuar")
                    flg_muestra = False
                else:
                    print("Personaje creado")
                    input("Enter para continuar")
                    heroes[len(heroes) + 1] = {"nivel":nivel, "nombre": nombre, "clase":clase, "arma" : arma_personaje,
                                               "fuerza":estadistica_frz, "magia":estadistica_mag, "defensa":estadistica_def, "agilidad":estadistica_agi,
                                               "vida":estadistica_vid, "xp":0}
                    flg_muestra = False
        
        flg_menu0 = True
        flg_crear_pers = False
    
    #Creacion de arma 
    while flg_crear_arma:
        clase = 0
        nombre_arma = ""
        nombre_estadistica1 = ""
        nombre_estadistica2 = ""
        estadistica1 = 0
        estadistica2 = 0
        nombre_debufo = ""
        debuff = 0
        eleccion_clase_arma = ""
       
        flg_clase = True  

        keys_clases = list(clases.keys())
        for pasada in range(len(keys_clases)):
            cambios = False
            for i in range(len(keys_clases)-1-pasada):
                if clases[keys_clases[i]] > clases[keys_clases[i+1]]:
                    cambios = True
                    aux = keys_clases[i]
                    keys_clases[i] = keys_clases[i+1]
                    keys_clases[i+1] = aux
            if not cambios:
                break
        
        for i in range(len(keys_clases)):
            eleccion_clase_arma = eleccion_clase_arma + "{}) ".format(i + 1) + clases[keys_clases[i]] + "\n"

        while flg_clase:
            print(nueva_arma + eleccion_clase_arma)
            opc = input("Opcion:\n")
            if not opc.isdigit():
                print(formato_invalido_numeros)
                input("Enter para continuar")
            elif not int(opc) in range(1,len(clases) + 1):
                print(fuera_rango)
                input("Enter para continuar")
            else:
                opc = int(opc)
                print("Clase seleccionada {}".format(clases[keys_clases[opc-1]]))
                input("Enter para continuar")
                clase = keys_clases[opc-1]
                flg_clase = False
                flg_nombre = True
        
        while flg_nombre:
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
                flg_estadisticas = True
                flg_nombre = False
        

        contador_stats = 0
        while flg_estadisticas:
            if estadistica1 == 0 or estadistica2 == 0:
                print(eleccion_estadisticas_arma)
                opc = input("Opcion:\n")
                if not opc.isdigit():
                    print(formato_invalido_numeros)
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
                if dec_deb.upper() == "S":
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

                elif dec_deb.upper() == "N":
                    print("Las estadisticas del arma son:\n{} = {}\n{} = {}\n".format(nombre_estadistica1, estadistica1, nombre_estadistica2, estadistica2))
                    input("Enter para continuar")
                    flg_muestra = True
                    flg_estadisticas = False

                else:
                    print(formato_invalido_letras)
                    input("Enter para continuar")
        
        while flg_muestra:
            if debuff == 0:
                print("Esta es la nueva arma:\n" + muestra_arma.format(nombre_arma, clases[clase], nombre_estadistica1, estadistica1, nombre_estadistica2, estadistica2))
            
            else:
                print("Esta es la nueva arma:\n" + muestra_arma_deb.format(nombre_arma, clases[clase], nombre_estadistica1, estadistica1, nombre_estadistica2, estadistica2, nombre_debufo, debuff))

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
    
    #Editar personaje
    while flg_edit_pers:
        eleccion_pers = ""
        keys_heroes = list(heroes.keys())
        for pasada in range(len(keys_heroes)):
            cambios = False
            for i in range(len(keys_heroes) - 1 - pasada):
                if heroes[keys_heroes[i]]["nombre"].upper() > heroes[keys_heroes[i + 1]]["nombre"].upper():
                    cambios = True
                    aux = keys_heroes[i]
                    keys_heroes[i] = keys_heroes[i+1]
                    keys_heroes[i+1] = aux 
            if not cambios:
                break
        print(keys_heroes)
        for i in range(len(keys_heroes)):
           eleccion_pers = eleccion_pers + "{}) ".format(i + 1) + heroes[keys_heroes[i]]["nombre"] + "\n"
        eleccion_pers = eleccion_pers + str(len(keys_heroes)+1) + ")" + " Salir" + "\n"
        
        print(menu_personaje + eleccion_pers)
        opc = input("Opcion:\n")
        if not opc.isdigit():
            print(formato_invalido_numeros)
            input("Enter para continuar")
        elif not int(opc) in range(1, len(heroes) + 2):
            print(fuera_rango)
            input("Enter para continuar")
        else:
            opc_1 = int(opc)
            if opc_1 == len(heroes)+1:
                flg_menu3 = True
                flg_edit_pers =  False
            else:
                opc = int(opc)
                nombre = heroes[keys_heroes[opc-1]]["nombre"]
                print(pers_seleccion.format(nombre))
                opc_e = input("Opcion:\n")
                if not opc_e.isdigit():
                    print(formato_invalido_numeros)
                    input("Enter para continuar")
                elif not int(opc_e) in range(1, 4):
                    print(fuera_rango)
                    input("Enter para continuar")
                else:
                    opc_e = int(opc_e)
                    if opc_e == 1:
                        nuevo_nombre = input("Nuevo nombre:\n")
                        while not nuevo_nombre.isalpha():
                                print(formato_invalido_letras)
                                input("Enter to continue")
                                nuevo_nombre = input("Nuevo nombre:\n")
                        print("El nombre: {}\nHa combiado por: {}".format(nombre, nuevo_nombre))
                        input("Enter para continuar")
                        heroes[keys_heroes[opc-1]]["nombre"] = nuevo_nombre
                        flg_menu3 = True
                        flg_edit_pers = False
                    elif opc_e == 2:
                        while True:
                            eleccion_arma = ""
                            armas_disponible = []
                            clase = heroes[keys_heroes[opc-1]]["clase"]
                            keys_arma = list(armas.keys())
                            for pasada in range(len(keys_arma)):
                                cambios = False
                                for i in range(len(keys_arma)-1-pasada):
                                    if armas[keys_arma[i]]["nombre"] > armas[keys_arma[i+1]]["nombre"]:
                                        cambios = True
                                        aux = keys_arma[i]
                                        keys_arma[i] = keys_arma[i+1]
                                        keys_arma[i + 1] = aux
                                if not cambios:
                                    break

                            for i in range(len(keys_arma)):
                                if armas[keys_arma[i]]["clase"] == clase:
                                    armas_disponible.append(keys_arma[i])
                                    eleccion_arma = eleccion_arma + "{}) ".format(len(armas_disponible)) + armas[keys_arma[i]]["nombre"] + "\n"
                            eleccion_arma = eleccion_arma + "{}) Salir".format(len(armas_disponible)+1)

                            print(menu_arma + eleccion_arma)
                            opc_a = input("Seleciona la arma por cual quieres cambiar la tuya:\n")
                            if not opc_a.isdigit():
                                print(formato_invalido_numeros)
                                input("Enter para continuar")
                            elif not int(opc_a) in range(1,len(armas_disponible)+2):
                                print(fuera_rango)
                                input("Enter para continuar")
                            else:
                                opc_a = int(opc_a)
                                if opc_a == len(armas_disponible)+1:
                                    break
                                else:
                                    print("El arma a cambiado de {} a {}".format(armas[heroes[keys_heroes[opc-1]]["arma"]]["nombre"],armas[armas_disponible[opc_a-1]]["nombre"]))
                                    input("Enter para continuar")
                                    heroes[keys_heroes[opc-1]]["arma"]  = armas_disponible[opc_a-1]
                                    flg_menu3 = True
                                    flg_edit_pers = False
                    else:
                        flg_menu3 = True
                        flg_edit_pers = False
    
    #Editar armas
    while flg_edit_arma:
        eleccion_arma = ""
        keys_arma = list(armas.keys())
        for pasada in range(len(keys_arma)):
            cambios = False
            for i in range(len(keys_arma)-1-pasada):
                if armas[keys_arma[i]]["nombre"].upper() > armas[keys_arma[i+1]]["nombre"].upper():
                    cambios = True
                    aux = keys_arma[i]
                    keys_arma[i] = keys_arma[i+1]
                    keys_arma[i + 1] = aux
            if not cambios:
                break

        for i in range(len(keys_arma)):

            eleccion_arma = eleccion_arma + "{}) ".format(i+1) + armas[keys_arma[i]]["nombre"] + "\n"

        print(cabezera_eleccion_arma + eleccion_arma)
        opc = input("Opcion:\n")
        if not opc.isdigit():
            print(formato_invalido_numeros)
            input("Enter para continuar")
        elif not int(opc) in range(1,len(armas) + 2):
            print(fuera_rango)
            input("Enter para continuar")
        else:
            
            opc = int(opc)
            nombre = armas[keys_arma[opc-1]]["nombre"]

            print(arma_seleccion.format(nombre))
            opc_e = input("Opcion:\n")

            if not opc_e.isdigit():
                print(formato_invalido_numeros)
                input("Enter para continuar")
            elif not int(opc_e) in range(1,3):
                print(fuera_rango)
                input("Enter para continuar")
            else:
                

                opc_e = int(opc_e)
                if opc_e == 1:
                    nuevo_nombre = input("Nuevo nombre:\n")
                    while not nuevo_nombre.isalpha():
                            print(formato_invalido_letras)
                            input("Enter to continue")
                            nuevo_nombre = input("Nuevo nombre:\n")

                    print("El nombre: {}\nHa combiado por: {}".format(nombre,nuevo_nombre))
                    input("Enter para continuar")
                    armas[keys_arma[opc-1]]["nombre"] = nuevo_nombre
                    flg_menu3 = True
                    flg_edit_arma = False
                else:
                    flg_menu3 = True
                    flg_edit_arma = False
