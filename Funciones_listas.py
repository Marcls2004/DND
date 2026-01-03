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
    3: {"nombre": "Golem", "fuerza": 30, "defensa": 20, "vida": 250,"xp_ganado":350},
    4: {"nombre": "Dragón anciano", "fuerza": 40, "defensa": 25, "vida": 500,"xp_ganado":800},
    5: {"nombre": "Señor demonio", "fuerza": 45, "defensa": 30, "vida": 600,"xp_ganado":1200}
}
def funcion_personaje(criterio,orden="asc"):
    lista = list(heroes)
    for pasada in range(len(lista)-1):
        cambios = False
        for i in range(len(lista)-pasada-1):
            if criterio == "id":
                if orden == "asc":
                    if lista[i] > lista[i + 1]:
                        lista[i], lista[i + 1] = lista[i + 1], lista[i]
                        cambios = True
                else:
                    if lista[i] < lista[i + 1]:
                        lista[i], lista[i + 1] = lista[i + 1], lista[i]
                        cambios = True
            elif criterio == "nombre":
                if orden == "asc":
                    if heroes[lista[i]]["nombre"] > heroes[lista[i+1]]["nombre"]:
                        lista[i], lista[i + 1] = lista[i + 1], lista[i]
                        cambios = True
                else:
                    if heroes[lista[i]]["nombre"] < heroes[lista[i+1]]["nombre"]:
                        lista[i], lista[i + 1] = lista[i + 1], lista[i]
                        cambios = True
            else:
                if orden == "asc":
                    hero_a_id = lista[i]
                    hero_b_id = lista[i + 1]

                    fuerza_a = heroes[hero_a_id][criterio]
                    id_arma_a = heroes[hero_a_id]["arma"]

                    caracts_a = armas[id_arma_a].get("caracteristicas", {})
                    fuerza_a += caracts_a.get(criterio, 0)

                    debuffos_a = armas[id_arma_a].get("debuffo", {})
                    fuerza_a += debuffos_a.get(criterio, 0)

                    fuerza_b = heroes[hero_b_id][criterio]
                    id_arma_b = heroes[hero_b_id]["arma"]

                    caracts_b = armas[id_arma_b].get("caracteristicas", {})
                    fuerza_b += caracts_b.get(criterio, 0)

                    debuffos_b = armas[id_arma_b].get("debuffo", {})
                    fuerza_b += debuffos_b.get(criterio, 0)
                    if fuerza_a < fuerza_b:
                        lista[i], lista[i + 1] = lista[i + 1], lista[i]
                        cambios = True
                else:
                    hero_a_id = lista[i]
                    hero_b_id = lista[i + 1]

                    fuerza_a = heroes[hero_a_id][criterio]
                    id_arma_a = heroes[hero_a_id]["arma"]

                    caracts_a = armas[id_arma_a].get("caracteristicas", {})
                    fuerza_a += caracts_a.get(criterio, 0)

                    debuffos_a = armas[id_arma_a].get("debuffo", {})
                    fuerza_a += debuffos_a.get(criterio, 0)

                    fuerza_b = heroes[hero_b_id][criterio]
                    id_arma_b = heroes[hero_b_id]["arma"]

                    caracts_b = armas[id_arma_b].get("caracteristicas", {})
                    fuerza_b += caracts_b.get(criterio, 0)

                    debuffos_b = armas[id_arma_b].get("debuffo", {})
                    fuerza_b += debuffos_b.get(criterio, 0)
                    if fuerza_a < fuerza_b:
                        lista[i], lista[i + 1] = lista[i + 1], lista[i]
                        cambios = True
        if not cambios:
            break
    return lista



def saber_lista_de_monstruos(nombre_lista,lista_mosntruos):
    nombre = nombre_lista
    opc2 = lista_mosntruos
    lista = list(lista_mosntruos)
    print("{}".format(nombre).center(40, "=") + "\n" + \
                      "1) Por vida" + "\n" + \
                      "2) Por ataque" + "\n" + \
                      "3) Por defensa" + "\n" + \
                      "4) Volver" )
    return opc2,lista

#opc2,lista = saber_lista_de_monstruos("monstruos_oscuros",monstruos_oscuros)

def listar_monstruos(lista,criterio,opc2,orden="asc"):
    lista = lista
    for pasadas in range(len(lista)):
        cambios = False
        for i in range(len(lista) - 1 - pasadas):
            if  orden == "asc":
                if opc2[lista[i]][criterio] < opc2[lista[i + 1]][criterio]:
                    lista[i], lista[i + 1] = lista[i + 1], lista[i]
                    cambios = True
            else:
                if opc2[lista[i]][criterio] < opc2[lista[i + 1]][criterio]:
                    lista[i], lista[i + 1] = lista[i + 1], lista[i]
                    cambios = True
        if not cambios:
            break
    return lista
#print(listar_monstruos(lista,"fuerza",opc2))


def listar_armas(criterio,orden = "asc"):
    lista = list(armas)
    if criterio not in ("id","nombre"):
        lista_filtrada = []
        for key in lista:
            if criterio in armas[key].get("caracteristicas", {}) or \
                    criterio in armas[key].get("debuffo", {}):
                lista_filtrada.append(key)
        lista = lista_filtrada
    for pasada in range(len(lista)-1):
        cambios = False
        for i in range(len(lista)-pasada-1):
            if criterio == "Id":
                if orden == "asc":
                    if lista[i] > lista[i + 1]:
                        lista[i], lista[i + 1] = lista[i + 1], lista[i]
                        cambios = True
                else:
                    if lista[i] < lista[i + 1]:
                        lista[i], lista[i + 1] = lista[i + 1], lista[i]
                        cambios = True
            elif criterio == "nombre":
                if orden == "asc":
                    if armas[lista[i]]["nombre"] >armas[lista[i+1]]["nombre"]:
                        lista[i], lista[i + 1] = lista[i + 1], lista[i]
                        cambios = True
                else:
                    if armas[lista[i]]["nombre"] <armas[lista[i+1]]["nombre"]:
                        lista[i], lista[i + 1] = lista[i + 1], lista[i]
                        cambios = True
            else:

                valor1 = armas[lista[i]].get("debuffo", {}).get(criterio,
                                                                        armas[lista[i]].get(
                                                                            "caracteristicas", {}).get(
                                                                            criterio, 0))
                valor2 = armas[lista[i + 1]].get("debuffo", {}).get(criterio,
                                                                            armas[lista[i + 1]].get(
                                                                                "caracteristicas", {}).get(
                                                                                criterio, 0))
                if orden == "asc":
                    if valor1 < valor2:
                        lista[i], lista[i + 1] = lista[i + 1], lista[i]
                        cambios = True
                else:
                    if valor1 >valor2:
                        lista[i], lista[i + 1] = lista[i + 1], lista[i]
                        cambios = True
        if not cambios:
            break
    return lista

print(listar_armas("fuerza"))