
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



def funcion_monstruos(nombre,criterio,orden):



