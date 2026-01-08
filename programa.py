import random
import time
from Funciones_Rol.Funciones_listas import funcion_armas
from Funciones_Rol.Funciones_menu import *
from Funciones_Rol.Funciones_editar import *
from Funciones_Rol.Funciones_listas import *
from Funciones_Rol.Variables_del_proyecto import *
from Funciones_Rol.Funciones_crear import *

while not flg_salir:
    while flg_menu0:
        
        opc = gen_menu(menu0)
        if opc == 1:
            resultado = ""
            for letra in introduccion:
                resultado = resultado + letra
                print("\r" + resultado, end = "")
                time.sleep(0.1)
            input("\n\nPulsa ENTER para continuar")
            heroe = ""
            menu_personaje["opciones"] = ""
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
            
            for i in range(len(keys_heroes)):
                menu_personaje["opciones"].append(heroes[keys_heroes[i]]["nombre"])
            
            resultado = ""
            for letra in seleccion_heroe:
                resultado = resultado + letra
                print("\r" + resultado, end = "")
                time.sleep(0.1)
            flg_jugar = True
            flg_menu0 = False
            pisos = 1
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
        #--------------------Esto es solo para el juego no se puede utilizar en el servidor (PARTE2)--------------------
        #INICIO
        
        #SELECCIONAR HEROE
        while heroe == "":
            """
            HAY QUE HACER UNO EXCLUSIVO PARA ESTO
            """
            opc = gen_menu(menu_personaje)
            
            heroe = heroes[keys_heroes[opc-1]]
            arma = armas[heroe["arma"]]
            arma_guardado = [[],[]]
            guardado_heroe = [heroes[keys_heroes[opc-1]]["nivel"],heroes[keys_heroes[opc-1]]["fuerza"],heroes[keys_heroes[opc-1]]["magia"],heroes[keys_heroes[opc-1]]["defensa"],heroes[keys_heroes[opc-1]]["agilidad"],heroes[keys_heroes[opc-1]]["vida"]]
            print(seleccionar_heroe.format(heroe["nombre"]))
            
            for key in arma["características"]:
                arma_guardado[0].append(arma["características"][key])

            if "debuffo" in arma:
                arma_guardado[1].append(arma["debuffo"])


            stats_personaje = [0,0,0,0,0]

            caracts = armas[heroe["arma"]].get("características", {})
            stats_personaje[0] += caracts.get("fuerza", 0)
            stats_personaje[1] += caracts.get("magia", 0)
            stats_personaje[2] += caracts.get("defensa", 0)
            stats_personaje[3] += caracts.get("agilidad", 0)
            stats_personaje[4] += caracts.get("vida", 0)

            debuffos = armas[heroe["arma"]].get("debuffo", {})
            stats_personaje[0] += debuffos.get("fuerza", 0)
            stats_personaje[1] += debuffos.get("magia", 0)
            stats_personaje[2] += debuffos.get("defensa", 0)
            stats_personaje[3] += debuffos.get("agilidad", 0)
            stats_personaje[4] += debuffos.get("vida", 0)

            limite_nivel = 100
            if heroe["nivel"] > 1:
                limite_nivel = 100 * (1.15 ** (heroe["nivel"] - 1))
                for i in range(1):
                    heroe["fuerza"] = heroe["fuerza"] * (1.0 + (random.randrange(30,140))/1000)
                    heroe["magia"] = heroe["magia"] * (1.0 + (random.randrange(30,140))/1000)
                    heroe["defensa"] = heroe["defensa"] * (1.0 + (random.randrange(30,140))/1000)
                    heroe["agilidad"] = heroe["agilidad"] * (1.0 + (random.randrange(30,140))/1000)
                    heroe["vida"] = heroe["vida"] * (1.0 + (random.randrange(30,140))/1000)

        #SELECCION DE ENEMIGO
        monstruo = ""
        if pisos <= 10:
            monstruo = monstruos_debiles[random.randint(1,4)]
        elif pisos <= 20:
            monstruo = bestias[random.randint(1,4)]
        elif pisos <= 30:
            monstruo = monstruos_enemigos_humanoides[random.randint(1,4)]
        elif pisos <= 40:
            monstruo = monstruos_oscuros[random.randint(1,4)]
        elif pisos <= 50:
            monstruo = criaturas_magicas[random.randint(1,4)]
        elif pisos <= 60:
            monstruo = monstruos_jefes[random.randint(1,4)]
        else:
            resultado = ""
            for letra in finalizacion:
                resultado += letra
                print("\r" + resultado, end="")
                time.sleep(0.1)
            input("\n\nPulsa ENTER para continuar")

        monstruo_guardado = [monstruo["vida"], monstruo["fuerza"], monstruo["defensa"], monstruo["xp_ganado"]]

        resultado = ""
        informacion = "En el piso {} te enfrentaras a {}".format(pisos,monstruo["nombre"])
        for letra in informacion:
            resultado += letra
            print("\r" + resultado, end="")
            time.sleep(0.1)
        input("\n\nPulsa ENTER para continuar")

        #subida de stats de monstruo para dificultad
        if pisos > 1:
            if pisos % 10 == 0:
                monstruo["vida"] = monstruo["vida"] * (1.50 ** pisos)
                monstruo["fuerza"] = monstruo["fuerza"] * (1.50 ** pisos)
                monstruo["defensa"] = monstruo["defensa"] * (1.50 ** pisos)
                monstruo["xp_ganado"] = monstruo["xp_ganado"] * (2.00 ** pisos)
            else:
                if pisos % 5 == 0:
                    monstruo["vida"] = monstruo["vida"] * (1.30 ** pisos)
                    monstruo["fuerza"] = monstruo["fuerza"] * (1.30 ** pisos)
                    monstruo["defensa"] = monstruo["defensa"] * (1.30 ** pisos)
                    monstruo["xp_ganado"] = monstruo["xp_ganado"] * (1.50 ** pisos)
                else:
                    monstruo["vida"] = monstruo["vida"] * (1.10 ** pisos)
                    monstruo["fuerza"] = monstruo["fuerza"] * (1.10 ** pisos)
                    monstruo["defensa"] = monstruo["defensa"] * (1.10 ** pisos)

        ataca = False
        defensa_total_mon = int(monstruo["defensa"])
        fuerza_total_mon = int(monstruo["fuerza"])
        vida_total_mon = int(monstruo["vida"])
        
        turno = 1
        cooldown_principal = 0
        cooldown_ultimate = 0
        vida_total = int(heroe["vida"] + stats_personaje[4])
        fuerza_total = int(heroe["fuerza"] + stats_personaje[0])
        magia_total = int(heroe["magia"] + stats_personaje[1])
        defensa_total = int(heroe["defensa"] + stats_personaje[2])
        agilidad_total = int(heroe["agilidad"] + stats_personaje[3])


        while vida_total_mon > 0 and vida_total > 0:
            while True:
                print(info_turno.format(turno,habilidades[clases[heroe["clase"]]]["basico"]["nombre"],habilidades[clases[heroe["clase"]]]["principal"]["nombre"],habilidades[clases[heroe["clase"]]]["ultimate"]["nombre"])
                    + "Nivel: {}\nVida: {}".format(str(heroe["nivel"]),str(vida_total)))
                opc = input("Opcion:\n")
                if not opc.isdigit():
                    print(formato_invalido_numeros)
                elif not int(opc) in range(1,4):
                    print(fuera_rango)
                else:
                    opc = int(opc)

                    if opc == 3:
                        if cooldown_ultimate == 0:
                            daño = (fuerza_total + magia_total ) * 5
                            cooldown_ultimate = cooldown_ultimate + 5
                            break
                        else:
                            print(en_cooldown + "\nQuedan {} turnos.".format(cooldown_ultimate))
                    elif opc == 2:
                        if cooldown_principal == 0:
                            daño = (fuerza_total + magia_total ) * 2
                            cooldown_principal = cooldown_principal + 3
                            break
                        else:
                            print(en_cooldown + "\nQuedan {} turnos.".format(cooldown_principal))
                    else:
                        daño = fuerza_total + magia_total
                        break

            if vida_total_mon - (daño - defensa_total_mon) <= 0:
                print("Has matado al enemigo. FELICIDADES!!!")
                input("Enter para continuar")
                vida_total_mon = 0
                break
            else:
                daño_real = daño - defensa_total_mon
                if daño_real < 0:
                    daño_real = 0

                vida_total_mon = vida_total_mon - daño_real
                ataca = True
            
            resultado = ""
            for letra in atacas.format(monstruo["nombre"],daño_real,vida_total_mon):
                resultado += letra
                print("\r" + resultado, end="")
                time.sleep(0.1)
            input("\n\nPulsa ENTER para continuar")

            if ataca:
                daño_mon = fuerza_total_mon
                if vida_total - (daño_mon - defensa_total ) <= 0:
                    print("Has muerto...")
                    input("Enter para continuar")
                    vida_total = 0
                    break
                else:
                    daño_real = daño_mon - defensa_total
                    if daño_real < 0:
                        print("hola")
                        daño_real = 0

                    vida_total = vida_total - daño_real
                    ataca = False
                
            resultado = ""
            texto = atacan.format(monstruo["nombre"],daño_real,vida_total)
            for letra in texto:
                resultado += letra
                print("\r" + resultado, end="")
                time.sleep(0.1)
            input("\n\nPulsa ENTER para continuar")

            turno = turno + 1
            if cooldown_ultimate != 0:
                cooldown_ultimate = cooldown_ultimate -1
            if cooldown_principal != 0:
                cooldown_principal = cooldown_principal -1 

        if vida_total == 0:
            resultado = ""
            finalizacion = "JAJAJAJAJA... Ya sabia yo que te ibas a morir en piso {}".format(str(pisos))
            for letra in finalizacion:
                resultado += letra
                print("\r" + resultado, end="")
                time.sleep(0.1)
            input("\n\nPulsa ENTER para continuar")
            
            heroe["xp"] = 0
            heroe["nivel"] = guardado_heroe[0]
            heroe["fuerza"] = guardado_heroe[1]
            heroe["magia"] = guardado_heroe[2]
            heroe["defensa"] = guardado_heroe[3]
            heroe["agilidad"] = guardado_heroe[4]
            heroe["vida"] = guardado_heroe[5]

            car = 0
            for key in arma["características"]:
                arma["características"][key] = arma_guardado[0][car]
                car = car + 1
            if "debuffo" in arma:
                car = 0
                for key in arma["debuffo"]:
                    arma["debuffo"][key] = arma_guardado[1][car]
                    car = car + 1

            flg_menu0 = True
            flg_jugar = False
        else:
            #derrota de monstruo
            heroe["xp"] = heroe["xp"] + monstruo["xp_ganado"]
            monstruo["vida"] = monstruo_guardado[0]
            monstruo["fuerza"] = monstruo_guardado[1]
            monstruo["defensa"] = monstruo_guardado[2]
            monstruo["xp_ganado"] = monstruo_guardado[3]

            #recompensa/subida de piso     
            rec_piso = rec_piso * (1.12 ** (pisos-1))
            pisos = pisos + 1
            heroe["xp"] = heroe["xp"] + rec_piso
            
            #subida de nivel
            while heroe["xp"] > limite_nivel:
                heroe["xp"] = heroe["xp"] - limite_nivel
                heroe["nivel"] = heroe["nivel"] + 1 
                limite_nivel = 100 * (1.15 ** (heroe["nivel"] - 1))
                print("Subida de nivel!!!")
                input("Enter para continuar")
                heroe["fuerza"] = heroe["fuerza"] * 1 + ((random.randrange(30,140))/1000)
                heroe["magia"] = heroe["magia"] * 1 + ((random.randrange(30,140))/1000)
                heroe["defensa"] = heroe["defensa"] * 1 + ((random.randrange(30,140))/1000)
                heroe["agilidad"] = heroe["agilidad"] * 1 + ((random.randrange(30,140))/1000)
                heroe["vida"] = heroe["vida"] * 1 + ((random.randrange(30,140))/1000)
                    
            #subida de stats de arma
            for key in arma["características"]:
                arma["características"][key] = arma["características"][key] * (1 + heroe["nivel"] * 0.05)
            if "debuffo" in arma:
                for key in arma["debuffo"]:
                    arma["debuffo"][key] = arma["debuffo"][key] * (1 + heroe["nivel"] * 0.05)

    # Elegir que crear
    while flg_menu2:
        opc = gen_menu(menu2)
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
        opc = gen_menu(menu3)
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
        opc = gen_menu(menu4)
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
    # Al listar tambien le sumamos las stats de armas
    while flg_menu41:
        opc = gen_menu(listar_personajes)
        
        if opc in range(1, 9):
            lista_ordenar = []
            for key in heroes:
                lista_ordenar.append(key)

            if opc == 1:
                lista_ordenar = funcion_personaje("id", orden="asc")
            elif opc == 2:
                lista_ordenar = funcion_personaje("nombre", orden="asc")
            elif opc == 3:
                lista_ordenar = funcion_personaje("fuerza", orden="des")
            elif opc == 4:
                lista_ordenar = funcion_personaje("magia", orden="des")
            elif opc == 5:
                lista_ordenar = funcion_personaje("defensa", orden="des")
            elif opc == 6:
                lista_ordenar = funcion_personaje("agilidad", orden="des")
            elif opc == 7:
                lista_ordenar = funcion_personaje("vida", orden="des")
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

                    caracts = armas[id_arma].get("características", {})
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

    # Listar armas
    while flg_menu42:

        opc = gen_menu(listar_armas)

        lista_ordenar = []
        propiedad_ordenar = ""

        for key in armas:
            lista_ordenar.append(key)

        if opc == 1:
            propiedad_ordenar = "ID"
            lista_ordenar = funcion_armas("id", orden="asc")

        elif opc == 2:
            propiedad_ordenar = "nombre"
            lista_ordenar = funcion_armas("nombre", orden="asc")

        elif opc == 3:
            propiedad_ordenar = "fuerza"
            lista_ordenar = funcion_armas("fuerza", orden="asc")

        elif opc == 4:
            propiedad_ordenar = "magia"
            lista_ordenar = funcion_armas("magia", orden="asc")

        elif opc == 5:
            propiedad_ordenar = "defensa"
            lista_ordenar = funcion_armas("defensa", orden="asc")

        elif opc == 6:
            propiedad_ordenar = "agilidad"
            lista_ordenar = funcion_armas("agilidad", orden="asc")

        elif opc == 7:
            flg_menu4 = True
            flg_menu42 = False

        if flg_menu42 and lista_ordenar:
            encabezado_ranking_armas = (
                    "Ranking Armas por {}".format(propiedad_ordenar.capitalize()).center(80, "=") + "\n" +
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
                caract = arma.get("características", {})
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
                fuerza_val = str(fuerza_efectiva) if (fuerza_base != 0 or fuerza_debuffo != 0) else "-"

                magia_efectiva = magia_base + magia_debuffo
                magia_val = str(magia_efectiva) if (magia_base != 0 or magia_debuffo != 0) else "-"

                defensa_efectiva = defensa_base + defensa_debuffo
                defensa_val = str(defensa_efectiva) if (defensa_base != 0 or defensa_debuffo != 0) else "-"

                agilidad_efectiva = agilidad_base + agilidad_debuffo
                agilidad_val = str(agilidad_efectiva) if (agilidad_base != 0 or agilidad_debuffo != 0) else "-"

                vida_val = str(vida_debuffo) if vida_debuffo != 0 else "-"

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
        cabezera = ""
        opc = gen_menu(menu_lista_monstruos)

        if opc == 1:
            cabezera = "Monstruos Debiles"
            opc2, lista, nombre = saber_lista_de_monstruos("Monstruos Debiles", monstruos_debiles)
        elif opc == 2:
            cabezera = "Bestias"
            opc2, lista, nombre = saber_lista_de_monstruos("Bestias", bestias)
        elif opc == 3:
            cabezera = "Monstruo Humanoides"
            opc2, lista, nombre = saber_lista_de_monstruos("Monstruo Enemigos Humanoides",
                                                           monstruos_enemigos_humanoides)
        elif opc == 4:
            cabezera = "Monstruos Oscuros"
            opc2, lista, nombre = saber_lista_de_monstruos("Monstruos Oscuros", monstruos_oscuros)
        elif opc == 5:
            cabezera = "Criaturas Magicas"
            opc2, lista, nombre = saber_lista_de_monstruos("Criaturas Magicas", criaturas_magicas)
        elif opc == 6:
            cabezera = "Jefes"
            opc2, lista, nombre = saber_lista_de_monstruos("Jefes", monstruos_jefes)
        else:
            flg_menu4 = True
            flg_menu43 = False
            continue

        opc = gen_menu({"cabezera":cabezera,"opciones":["Ordenar por Vida", "Ordenar por Fuerza", "Ordenar por Defensa", "Salir"]})

        if opc == 1:
            lista_ordenar = funcion_monstruos(lista, "vida", opc2, orden="asc")
        elif opc == 2:
            lista_ordenar = funcion_monstruos(lista, "fuerza", opc2, orden="asc")
        elif opc == 3:
            lista_ordenar = funcion_monstruos(lista, "defensa", opc2, orden="asc")
        else:
            flg_menu4 = True
            flg_menu43 = False
            continue

        if flg_menu43:
            encabezado_ranking_monstruos = (
                    ("Ranking " + nombre).center(50, "=") + "\n" +
                    "Id".ljust(5) +
                    "Nombre".ljust(25) +
                    "Fuerza".ljust(8) +
                    "Defensa".ljust(8) +
                    "Vida".ljust(8)
            )

            print(encabezado_ranking_monstruos)

            for i in range(len(opc2)):
                print(
                    str(lista_ordenar[i]).ljust(5) +
                    str(opc2[lista_ordenar[i]]["nombre"]).ljust(25) +
                    str(opc2[lista_ordenar[i]]["fuerza"]).ljust(8) +
                    str(opc2[lista_ordenar[i]]["defensa"]).ljust(8) +
                    str(opc2[lista_ordenar[i]]["vida"]).ljust(8)
                )

            print("".center(50, "="))
            input("Enter")

    #Creacion de personaje
    while flg_crear_pers:
        nombre = ""
        nivel = 0
        arma_personaje = 0
        estadistica_frz = 0
        estadistica_mag = 0
        estadistica_def = 0
        estadistica_agi = 0
        estadistica_vid = 0
        eleccion_clase["opciones"] = []
        eleccion_arma["opciones"] = []
        armas_disponibles =[]
        stats = [0,0,0,0,0]

        nombre = nuevo_nombre_heroe()

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
            eleccion_clase["opciones"].append(clases[keys_clases[i]])

        selec_clase = clase(eleccion_clase,keys_clases)

        nivel = ini_nivel()
        
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
            if armas[id]["clase"] == selec_clase:
                armas_disponibles.append(id)
                eleccion_arma["opciones"].append(armas[id]["nombre"])

        arma_personaje = selec_arma(eleccion_arma,armas_disponibles)

        stats = selec_stats(stats)

        nuevo_heroe = mostrar_nuevo_heroe(nombre,selec_clase,nivel,arma_personaje,stats)

        if nuevo_heroe == "":
            flg_menu2 = True
            flg_crear_pers = False
        else:
            heroes[len(heroes) + 1] = nuevo_heroe
            flg_menu2 = True
            flg_crear_pers = False

    #Creacion de arma 
    while flg_crear_arma:
        clase_nueva_arma["opciones"] = [] 

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
            clase_nueva_arma["opciones"].append(clases[keys_clases[i]])

        selec_clase = clase(clase_nueva_arma,keys_clases)
        
        nombre_arma = nuevo_nombre_arma()

        estadisticas = nuevas_estadisticas_arma()

        nueva_arma = final_arma_nueva(nombre_arma,selec_clase,estadisticas)

        armas[len(armas) + 1] = nueva_arma                                   
                    
        flg_menu2 = True
        flg_crear_arma = False
    
    #Editar personaje
    while flg_edit_pers:

        keys_heroes = ordenar_y_generar_opciones(heroes, eleccion_pers)

        opc_1 = menu(eleccion_pers["opciones"])

        if opc_1 == len(heroes) + 1:
            flg_menu3 = True
            flg_edit_pers = False
            break

        nombre = heroes[keys_heroes[opc_1 - 1]]["nombre"]
        pers_seleccion["cabezera"] = pers_seleccion["cabezera"].format(nombre)

        opc_e = gen_menu(pers_seleccion)

        if opc_e == 1:
            heroes = editar_nombre(opc_1, keys_heroes, heroes)
            flg_menu3 = True
            flg_edit_pers = False

        elif opc_e == 2:
            while True:

                keys_arma = ordenar_y_generar_opciones(armas, eleccion_arma)

                eleccion_arma["opciones"] = []
                clase = heroes[keys_heroes[opc_1 - 1]]["clase"]

                for k in keys_arma:
                    if armas[k]["clase"] == clase:
                        eleccion_arma["opciones"].append(armas[k]["nombre"])

                eleccion_arma["opciones"].append("Salir")

                opc_a = menu(eleccion_arma["opciones"])

                if opc_a == len(eleccion_arma["opciones"]):
                    break

                nombre_arma_elegida = eleccion_arma["opciones"][opc_a - 1]

                clave_arma_elegida = None
                for k in armas:
                    if armas[k]["nombre"] == nombre_arma_elegida:
                        clave_arma_elegida = k
                        break

                clave_arma_actual = heroes[keys_heroes[opc_1 - 1]]["arma"]

                if armas[clave_arma_actual]["nombre"] == armas[clave_arma_elegida]["nombre"]:
                    print("Elegiste la misma arma")
                    input("Enter para continuar")
                    break

                print("El arma ha cambiado de {} a {}".format(
                    armas[clave_arma_actual]["nombre"],
                    armas[clave_arma_elegida]["nombre"]
                ))
                input("Enter para continuar")

                heroes[keys_heroes[opc_1 - 1]]["arma"] = clave_arma_elegida
                break
        else:
            pers_seleccion["cabezera"] = "Editar {}"
            flg_menu3 = True
            flg_edit_pers = False

    #Editar armas
    while flg_edit_arma:
        keys_arma = ordenar_y_generar_opciones(armas, eleccion_arma)

        opc = menu(eleccion_arma["opciones"])

        if opc == len(eleccion_arma["opciones"]):
            flg_edit_arma = False
            flg_menu3 = True
            break

        nombre = armas[keys_arma[opc - 1]]["nombre"]
        arma_seleccion["cabezera"] = arma_seleccion["cabezera"].format(nombre)

        opc_e = gen_menu(arma_seleccion)

        if opc_e == 1:
            armas = editar_nombre(opc, keys_arma, armas)
            flg_menu3 = True
            flg_edit_arma = False

        else:
            arma_seleccion["cabezera"] = "Editar {}"
            flg_menu3 = True
            flg_edit_arma = False
