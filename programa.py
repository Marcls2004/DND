import random
from Funciones_Rol.Funciones_menu import *
from Funciones_Rol.Funciones_crear import *
from Funciones_Rol.Variables import * 
import time

while not flg_salir:
    while flg_menu0:
        print(gen_menu(menu0))
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
            print("\n" + gen_menu(menu_personaje))
            opc = input("Selecciona con cual heroe quieres jugar:\n")

            while not opc.isdigit() or not int(opc) in range(1,len(heroes) + 1):
                print("Solo puedes seleccionar un heroe de la lista")
                opc = input("Selecciona con cual heroe quieres jugar:\n")
            opc = int(opc)
            
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
        print(gen_menu(menu2))
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
        print(gen_menu(menu3))
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
        print(gen_menu(menu4))
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
    # Al listar tambien le sumamos las stats de armas
    while flg_menu41:
        print(gen_menu(listar_personajes))
        opc = input("Opcion: \n")
        if opc.isdigit():
            opc = int(opc)
            if opc in range(1,9):
                lista_ordenar = []
                for key in heroes:
                    lista_ordenar.append(key)
                if opc == 1:
                    #Listamos por id de personaje
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
                    #Listamos por nombre de personaje
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
                    #Listamos por fuerza de personaje
                    for pasadas in range(len(lista_ordenar)):
                        cambios = False
                        for i in range(len(lista_ordenar) - 1 - pasadas):
                            hero_a_id = lista_ordenar[i]
                            hero_b_id = lista_ordenar[i + 1]

                            fuerza_a = heroes[hero_a_id]["fuerza"]
                            id_arma_a = heroes[hero_a_id]["arma"]

                            caracts_a = armas[id_arma_a].get("características", {})
                            fuerza_a += caracts_a.get("fuerza", 0)

                            debuffos_a = armas[id_arma_a].get("debuffo", {})
                            fuerza_a += debuffos_a.get("fuerza", 0)

                            fuerza_b = heroes[hero_b_id]["fuerza"]
                            id_arma_b = heroes[hero_b_id]["arma"]

                            caracts_b = armas[id_arma_b].get("características", {})
                            fuerza_b += caracts_b.get("fuerza", 0)

                            debuffos_b = armas[id_arma_b].get("debuffo", {})
                            fuerza_b += debuffos_b.get("fuerza", 0)
                            if fuerza_a < fuerza_b:
                                aux = lista_ordenar[i]
                                lista_ordenar[i] = lista_ordenar[i + 1]
                                lista_ordenar[i + 1] = aux
                                cambios = True
                        if not cambios:
                            break
                elif opc == 4:
                    #Listamos por magia
                    for pasadas in range(len(lista_ordenar)):
                        cambios = False
                        for i in range(len(lista_ordenar) - 1 - pasadas):
                            hero_a_id = lista_ordenar[i]
                            hero_b_id = lista_ordenar[i + 1]

                            magia_a = heroes[hero_a_id]["magia"]
                            id_arma_a = heroes[hero_a_id]["arma"]

                            caracts_a = armas[id_arma_a].get("características", {})
                            magia_a += caracts_a.get("magia", 0)

                            debuffos_a = armas[id_arma_a].get("debuffo", {})
                            magia_a += debuffos_a.get("magia", 0)

                            magia_b = heroes[hero_b_id]["magia"]
                            id_arma_b = heroes[hero_b_id]["arma"]

                            caracts_b = armas[id_arma_b].get("características", {})
                            magia_b += caracts_b.get("magia", 0)

                            debuffos_b = armas[id_arma_b].get("debuffo", {})
                            magia_b += debuffos_b.get("magia", 0)
                            if magia_a < magia_b:
                                aux = lista_ordenar[i]
                                lista_ordenar[i] = lista_ordenar[i + 1]
                                lista_ordenar[i + 1] = aux
                                cambios = True
                        if not cambios:
                            break
                elif opc == 5:
                    #Listamos por defensa
                    for pasadas in range(len(lista_ordenar)):
                        cambios = False
                        for i in range(len(lista_ordenar) - 1 - pasadas):
                            hero_a_id = lista_ordenar[i]
                            hero_b_id = lista_ordenar[i + 1]

                            defensa_a = heroes[hero_a_id]["defensa"]
                            id_arma_a = heroes[hero_a_id]["arma"]

                            caracts_a = armas[id_arma_a].get("características", {})
                            defensa_a += caracts_a.get("defensa", 0)

                            debuffos_a = armas[id_arma_a].get("debuffo", {})
                            defensa_a += debuffos_a.get("defensa", 0)

                            defensa_b = heroes[hero_b_id]["defensa"]
                            id_arma_b = heroes[hero_b_id]["arma"]

                            caracts_b = armas[id_arma_b].get("características", {})
                            defensa_b += caracts_b.get("defensa", 0)

                            debuffos_b = armas[id_arma_b].get("debuffo", {})
                            defensa_b += debuffos_b.get("defensa", 0)
                            if defensa_a < defensa_b:
                                aux = lista_ordenar[i]
                                lista_ordenar[i] = lista_ordenar[i + 1]
                                lista_ordenar[i + 1] = aux
                                cambios = True
                        if not cambios:
                            break
                elif opc == 6:
                    #Listamos por agilidad
                    for pasadas in range(len(lista_ordenar)):
                        cambios = False
                        for i in range(len(lista_ordenar) - 1 - pasadas):
                            hero_a_id = lista_ordenar[i]
                            hero_b_id = lista_ordenar[i + 1]

                            agilidad_a = heroes[hero_a_id]["agilidad"]
                            id_arma_a = heroes[hero_a_id]["arma"]

                            caracts_a = armas[id_arma_a].get("características", {})
                            agilidad_a += caracts_a.get("agilidad", 0)

                            debuffos_a = armas[id_arma_a].get("debuffo", {})
                            agilidad_a += debuffos_a.get("agilidad", 0)

                            agilidad_b = heroes[hero_b_id]["agilidad"]
                            id_arma_b = heroes[hero_b_id]["arma"]

                            caracts_b = armas[id_arma_b].get("características", {})
                            agilidad_b += caracts_b.get("agilidad", 0)

                            debuffos_b = armas[id_arma_b].get("debuffo", {})
                            agilidad_b += debuffos_b.get("agilidad", 0)
                            if agilidad_b < agilidad_b:
                                aux = lista_ordenar[i]
                                lista_ordenar[i] = lista_ordenar[i + 1]
                                lista_ordenar[i + 1] = aux
                                cambios = True
                        if not cambios:
                            break
                elif opc == 7:
                    #Listamos por vida
                    for pasadas in range(len(lista_ordenar)):
                        cambios = False
                        for i in range(len(lista_ordenar) - 1 - pasadas):
                            hero_a_id = lista_ordenar[i]
                            hero_b_id = lista_ordenar[i + 1]

                            vida_a = heroes[hero_a_id]["vida"]
                            id_arma_a = heroes[hero_a_id]["arma"]

                            caracts_a = armas[id_arma_a].get("características", {})
                            vida_a += caracts_a.get("vida", 0)

                            debuffos_a = armas[id_arma_a].get("debuffo", {})
                            vida_a += debuffos_a.get("vida", 0)

                            vida_b = heroes[hero_b_id]["vida"]
                            id_arma_b = heroes[hero_b_id]["arma"]

                            caracts_b = armas[id_arma_b].get("características", {})
                            vida_b += caracts_b.get("vida", 0)

                            debuffos_b = armas[id_arma_b].get("debuffo", {})
                            vida_b += debuffos_b.get("vida", 0)
                            if vida_a < vida_b:
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
        else:
            print(formato_invalido_numeros)
            input("Enter para continuar")
    
    # Listar armas
    while flg_menu42:
        print(gen_menu(listar_armas))
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
                    if propiedad_ordenar in armas[key].get("características", {}) or \
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
                                                                                        "características", {}).get(
                                                                                        propiedad_ordenar, 0))
                            valor2 = armas[lista_ordenar[i + 1]].get("debuffo", {}).get(propiedad_ordenar,
                                                                                        armas[lista_ordenar[i + 1]].get(
                                                                                            "características", {}).get(
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
                    if propiedad_ordenar in armas[key].get("características", {}) or \
                            propiedad_ordenar in armas[key].get("debuffo", {}):
                        lista_filtrada.append(key)
                lista_ordenar = lista_filtrada

                if lista_ordenar:
                    for pasadas in range(len(lista_ordenar)):
                        cambios = False
                        for i in range(len(lista_ordenar) - 1 - pasadas):
                            valor1 = armas[lista_ordenar[i]].get("debuffo", {}).get(propiedad_ordenar,
                                                                                    armas[lista_ordenar[i]].get(
                                                                                        "características", {}).get(
                                                                                        propiedad_ordenar, 0))
                            valor2 = armas[lista_ordenar[i + 1]].get("debuffo", {}).get(propiedad_ordenar,
                                                                                        armas[lista_ordenar[i + 1]].get(
                                                                                            "características", {}).get(
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
                    if propiedad_ordenar in armas[key].get("características", {}) or \
                            propiedad_ordenar in armas[key].get("debuffo", {}):
                        lista_filtrada.append(key)
                lista_ordenar = lista_filtrada


                if lista_ordenar:
                    for pasadas in range(len(lista_ordenar)):
                        cambios = False
                        for i in range(len(lista_ordenar) - 1 - pasadas):
                            valor1 = armas[lista_ordenar[i]].get("debuffo", {}).get(propiedad_ordenar,
                                                                                    armas[lista_ordenar[i]].get(
                                                                                        "características", {}).get(
                                                                                        propiedad_ordenar, 0))
                            valor2 = armas[lista_ordenar[i + 1]].get("debuffo", {}).get(propiedad_ordenar,
                                                                                        armas[lista_ordenar[i + 1]].get(
                                                                                            "características", {}).get(
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
                    if propiedad_ordenar in armas[key].get("características", {}) or \
                            propiedad_ordenar in armas[key].get("debuffo", {}):
                        lista_filtrada.append(key)
                lista_ordenar = lista_filtrada


                if lista_ordenar:
                    for pasadas in range(len(lista_ordenar)):
                        cambios = False
                        for i in range(len(lista_ordenar) - 1 - pasadas):
                            valor1 = armas[lista_ordenar[i]].get("debuffo", {}).get(propiedad_ordenar,
                                                                                    armas[lista_ordenar[i]].get(
                                                                                        "características", {}).get(
                                                                                        propiedad_ordenar, 0))
                            valor2 = armas[lista_ordenar[i + 1]].get("debuffo", {}).get(propiedad_ordenar,
                                                                                        armas[lista_ordenar[i + 1]].get(
                                                                                            "características", {}).get(
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
        print(gen_menu(menu_lista_monstruos))
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
                nombre= "Bestias"
                opc2 = bestias
                lista_ordenar = []
                for key in bestias:
                    lista_ordenar.append(key)
            elif opc == 3:
                nombre= "Monstruo Enemigos Humanoides"
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
                
            listar_monstruos = {"cabezera":nombre,
                                "opciones":["1) Por vida",
                                            "2) Por ataque",
                                            "3) Por defensa",
                                            "4) Volver"]}
            print(gen_menu(listar_monstruos))
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
                    #Listamos por vida
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
                    #Listamos por fuerza
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
                    #Listamos por defensa
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
        arma_personaje = 0
        estadistica_frz = 0
        estadistica_mag = 0
        estadistica_def = 0
        estadistica_agi = 0
        estadistica_vid = 0
        eleccion_clase["opciones"] = []
        eleccion_arma["opciones"] = []

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
            eleccion_clase["opciones"].append(clases[keys_clases[i]])

        while flg_clase:
            print(gen_menu(eleccion_clase))
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
                eleccion_arma["opciones"].append(armas[id]["nombre"])

        while flg_arma:
            print(gen_menu(eleccion_arma))
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
                print(gen_menu(eleccion_estadisticas))
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
        clase_nueva_arma["opciones"] = []
       
        flg_clase = True  

        keys_clases = list(clases.keys())
        clases_ordenadas = burbuja(keys_clases,clases)
        
        for i in range(len(keys_clases)):
            clase_nueva_arma["opciones"].append(clases[clases_ordenadas[i]])

        while flg_clase:
            print(gen_menu(clase_nueva_arma))
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
                print(gen_menu(eleccion_estadisticas))
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
                        print("Esta característica ya la has elegido, elige otra.")
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
                                               "características":{nombre_estadistica1 : estadistica1, nombre_estadistica2 : estadistica2}}
                    else:
                        armas[len(armas) + 1] = {"clase" : clase, "nombre": nombre_arma,
                                               "características":{nombre_estadistica1 : estadistica1, nombre_estadistica2 : estadistica2},
                                               "debuffo":{nombre_debufo:debuff}}
                                        
                    flg_muestra = False
        flg_menu0 = True
        flg_crear_arma = False
    
    #Editar personaje
    while flg_edit_pers:

        menu_personaje["opciones"] = []
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
        menu_personaje["opciones"].append("Salir")
        
        print(gen_menu(menu_personaje))
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
                pers_seleccion["cabezera"] = pers_seleccion["cabezera"].format(nombre)
                print(gen_menu(pers_seleccion))
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
                        pers_seleccion["cabezera"] = "Editar {}"
                        flg_menu3 = True
                        flg_edit_pers = False
                    elif opc_e == 2:
                        while True:
                            eleccion_arma["opciones"] = []
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
                                    eleccion_arma["opciones"].append(armas[keys_arma[i]]["nombre"])
                            eleccion_arma["opciones"].append("Salir")

                            print(gen_menu(eleccion_arma))
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
                                    if armas[heroes[keys_heroes[opc-1]]["arma"]]["nombre"] ==armas[armas_disponible[opc_a-1]]["nombre"]:
                                        print("Elegiste la misma arma ")
                                        input("Enter para continuar")
                                        break
                                    else:
                                        print("El arma a cambiado de {} a {}".format(
                                            armas[heroes[keys_heroes[opc - 1]]["arma"]]["nombre"],
                                            armas[armas_disponible[opc_a - 1]]["nombre"]))
                                        input("Enter para continuar")
                                        heroes[keys_heroes[opc - 1]]["arma"] = armas_disponible[opc_a - 1]
                                        break
                        pers_seleccion["cabezera"] = "Editar {}"
                    else:
                        pers_seleccion["cabezera"] = "Editar {}"
                        flg_menu3 = True
                        flg_edit_pers = False
    
    #Editar armas
    while flg_edit_arma:
        eleccion_arma["opciones"] = []
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
            eleccion_arma["opciones"].append(armas[keys_arma[i]]["nombre"]) 

        print(gen_menu(eleccion_arma))
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
            arma_seleccion["cabezera"] = arma_seleccion["cabezera"].format(nombre)

            print(gen_menu(arma_seleccion))
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
                    arma_seleccion["cabezera"] = "Editar {}"
                    flg_menu3 = True
                    flg_edit_arma = False
                else:
                    arma_seleccion["cabezera"] = "Editar {}"
                    flg_menu3 = True
                    flg_edit_arma = False
