from Funciones_Rol.Variables_del_proyecto import heroes,armas
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
                    if heroes[lista[i]]["nombre"].upper() > heroes[lista[i+1]]["nombre"].upper():
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
                    if fuerza_a > fuerza_b:
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



def saber_lista_de_monstruos(nombre_lista,lista_monstruos):
    nombre = nombre_lista
    opc2 = lista_monstruos
    lista = list(lista_monstruos)
    return opc2,lista,nombre

#opc2,lista = saber_lista_de_monstruos("monstruos_oscuros",monstruos_oscuros)

def funcion_monstruos(lista,criterio,opc2,orden="asc"):
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


def funcion_armas(criterio,orden = "asc"):
    lista = list(armas)
    if criterio not in ("id","nombre"):
        lista_filtrada = []
        for key in lista:
            if criterio in armas[key].get("características", {}) or \
                    criterio in armas[key].get("debuffo", {}):
                lista_filtrada.append(key)
        lista = lista_filtrada
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
                    if armas[lista[i]]["nombre"].upper() >armas[lista[i+1]]["nombre"].upper():
                        lista[i], lista[i + 1] = lista[i + 1], lista[i]
                        cambios = True
                else:
                    if armas[lista[i]]["nombre"] <armas[lista[i+1]]["nombre"]:
                        lista[i], lista[i + 1] = lista[i + 1], lista[i]
                        cambios = True
            else:

                valor1 = armas[lista[i]].get("debuffo", {}).get(criterio,
                                                                        armas[lista[i]].get(
                                                                            "características", {}).get(
                                                                            criterio, 0))
                valor2 = armas[lista[i + 1]].get("debuffo", {}).get(criterio,
                                                                            armas[lista[i + 1]].get(
                                                                                "características", {}).get(
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

#print(listar_armas("fuerza"))
