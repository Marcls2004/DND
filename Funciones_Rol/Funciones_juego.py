import time
import random
from Funciones_Rol.Funciones_menu import *
from Funciones_Rol.Variables_del_proyecto import *
from Funciones_Rol.Variables_del_proyecto import *
def escribir(texto):
    resultado = ""
    for letra in texto:
        resultado = resultado + letra
        print("\r" + resultado, end = "")
        time.sleep(0.1)
    return

def menu_seleccion(keys):
    opc = gen_menu(menu_personaje)
    heroe = heroes[keys[opc-1]]
    arma = armas[heroe["arma"]]
    print(seleccionar_heroe.format(heroe["nombre"]))     
    return heroe, arma

def heroe_seleccionado(heroe,limite):
    if heroe["nivel"] > 1:
        limite = 100 * (1.15 ** (heroe["nivel"] - 1))
        for i in range(1):
            heroe["fuerza"] = heroe["fuerza"] * (1.0 + (random.randrange(30,140))/1000)
            heroe["magia"] = heroe["magia"] * (1.0 + (random.randrange(30,140))/1000)
            heroe["defensa"] = heroe["defensa"] * (1.0 + (random.randrange(30,140))/1000)
            heroe["agilidad"] = heroe["agilidad"] * (1.0 + (random.randrange(30,140))/1000)
            heroe["vida"] = heroe["vida"] * (1.0 + (random.randrange(30,140))/1000)
    return heroe,limite

def mon_seleccionar(pisos):
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

    monstruo_guardado = [monstruo["vida"], monstruo["fuerza"], monstruo["defensa"], monstruo["xp_ganado"]]

    informacion = "En el piso {} te enfrentaras a {}".format(pisos,monstruo["nombre"])
    escribir(informacion)
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
    return monstruo,monstruo_guardado

def kill_mon(heroe,monstruo,monstruo_guardado):
    heroe["xp"] = heroe["xp"] + monstruo["xp_ganado"]
    monstruo["vida"] = monstruo_guardado[0]
    monstruo["fuerza"] = monstruo_guardado[1]
    monstruo["defensa"] = monstruo_guardado[2]
    monstruo["xp_ganado"] = monstruo_guardado[3]
    return heroe,monstruo

def pasarse_piso(recompensa,piso,heroe):         
    recompensa = recompensa * (1.12 ** (piso-1))
    piso = piso + 1
    heroe["xp"] = heroe["xp"] + recompensa
    return recompensa,piso,heroe

def subir_nivel(heroe,limite_nivel):
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
    return heroe,limite_nivel

def habilidades_activas():
    return

def jugar(rec_piso,heroe):
    while True:
        #INTRODUCCION ENTRE VARIAS COSAS
        escribir(introduccion)
        input("\n\nPulsa ENTER para continuar")

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

        escribir(seleccion_heroe)
        input("\n\nPulsa ENTER para continuar")

        # print("\n")
        
        #SELECCIONAR HEROE    
        if heroe == "":
            heroe,arma = menu_seleccion(keys_heroes)
        
            guardado_heroe = {"nivel":heroe["nivel"],"fuerza":heroe["fuerza"],"magia":heroe["magia"],"defensa":heroe["defensa"],"agilidad":heroe["agilidad"],"vida":heroe["vida"]}
            arma_guardado = [[],[]]
            for key in arma["características"]:
                arma_guardado[0].append(arma["características"][key])

            if "debuffo" in arma:
                arma_guardado[1].append(arma["debuffo"])

        
            limite = 100
            stats_personaje = [0,0,0,0,0]
            pisos = 1

            heroe,limite = heroe_seleccionado(heroe,limite)

        #FINALIZACION
        if pisos > 60:
            escribir(finalizacion)
            input("\n\nPulsa ENTER para continuar")
        else:

            #SELECCION DE ENEMIGO
            monstruo,monstruo_guardado = mon_seleccionar(pisos)

            ataca = False
            defensa_total_mon = int(monstruo["defensa"])
            fuerza_total_mon = int(monstruo["fuerza"])
            vida_total_mon = int(monstruo["vida"])
            
            turno = 1
            cooldown_principal = 0
            cooldown_ultimate = 0
            stats_personaje = [0,0,0,0,0]

            #subida de stats de arma
            for key in arma["características"]:
                arma["características"][key] = arma["características"][key] * (1 + heroe["nivel"] * 0.05)
            if "debuffo" in arma:
                for key in arma["debuffo"]:
                    arma["debuffo"][key] = arma["debuffo"][key] * (1 + heroe["nivel"] * 0.05)  

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
                
                escribir(atacas.format(monstruo["nombre"],daño_real,vida_total_mon))
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
                    
                escribir(atacan.format(monstruo["nombre"],daño_real,vida_total))
                input("\n\nPulsa ENTER para continuar")

                turno = turno + 1
                if cooldown_ultimate != 0:
                    cooldown_ultimate = cooldown_ultimate -1
                if cooldown_principal != 0:
                    cooldown_principal = cooldown_principal -1 

            if vida_total == 0:
                finalizacion = "JAJAJAJAJA... Ya sabia yo que te ibas a morir en piso {}".format(str(pisos))
                escribir(finalizacion)
                input("\n\nPulsa ENTER para continuar")
                
                heroe["xp"] = 0
                heroe["nivel"] = guardado_heroe["nivel"]
                heroe["fuerza"] = guardado_heroe["fuerza"]
                heroe["magia"] = guardado_heroe["magia"]
                heroe["defensa"] = guardado_heroe["defensa"]
                heroe["agilidad"] = guardado_heroe["agilidad"]
                heroe["vida"] = guardado_heroe["vida"]
                monstruo["vida"] = monstruo_guardado[0]
                monstruo["fuerza"] = monstruo_guardado[1]
                monstruo["defensa"] = monstruo_guardado[2]
                monstruo["xp_ganado"] = monstruo_guardado[3]

                car = 0
                for key in arma["características"]:
                    arma["características"][key] = arma_guardado[0][car]
                    car = car + 1
                if "debuffo" in arma:
                    car = 0
                    for key in arma["debuffo"]:
                        arma["debuffo"][key] = arma_guardado[1][car]
                        car = car + 1
                return
            
            else:
                #derrota de monstruo
                heroe,monstruo = kill_mon(heroe,monstruo,monstruo_guardado)

                #recompensa/subida de piso
                rec_piso,pisos,heroe = pasarse_piso(rec_piso,pisos,heroe)

                #subida de nivel / subida stats arma
                heroe,limite = subir_nivel(heroe,limite)