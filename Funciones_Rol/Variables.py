introduccion = "Hola viajero, para salir de aqui tendras que ir derrotando todos los enemigos que te encuentres. Nos veremos en el piso final o no JAJAJAJAJAJAJA..."
seleccion_heroe = "Primero tendras que seleccionar el heroe con el que querras emprender esta aventura."
finalizacion = "Enhorabuena viajero has llegado al final, pero esto no se acaba aqui ya lo veras proximamente JAJAJAJAJAJAJA..."
#--------------------HABILIDADES--------------------
#esto no se pondra en el documento
rec_piso = 140
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
    "Cazador":{"basico":{"nombre":"Flecha precisa","daño":fuerza_total - (defensa_total_mon - perforacion_basica)},"principal":{"nombre":"Disparo perforante","daño":fuerza_total - (defensa_total_mon - perforacion_principal)},"ultimate":{"nombre":"Furia del titan","daño":fuerza_total - (defensa_total_mon - perforacion_ultimate)}},
    "Mago":{"basico":{"nombre":"Bola mágica","daño":magia_total},"principal":{"nombre":"Explosión arcana","daño":magia_total*1.5},"ultimate":{"nombre":"Tormenta elemental","daño":magia_total*2}},
    "Clérigo":{"basico":{"nombre":"Luz purificadora","daño":magia_total,"buff":vida_total + (magia_total//3)},"principal":{"nombre":"Bendicion sagrada","buff":defensa_total * 2},"ultimate":{"nombre":"Milagro divino","buff":vida_total + (magia_total//3) + (vida_total//3)}},
    "Druida":{"basico":{"nombre":"Látigo de enredaderas","daño":magia_total + (fuerza_total)//5},"principal":{"nombre":"Forma bestial","buff":[fuerza_total * 1.5,agilidad_total * 1.5]},"ultimate":{"nombre":"Espiritu del bosque","buff":[magia_total*1.5,vida_total*1.5]}},
    "Bardo":{"basico":{"nombre":"Nota disonante","daño":magia_total},"principal":{"nombre":"Canción inspiradora","buff":[magia_total*1.5,agilidad_total*1.5]},"ultimate":{"nombre":"Sinfonía legendaria","debuffo":defensa_total_mon - (defensa_total_mon//5),"buff":[magia_total*1.5,defensa_total*1.5,agilidad_total*1.5]}},
    "Monje":{"basico":{"nombre":"Puño rapido","daño":fuerza_total + agilidad_total},"principal":{"nombre":"Combo devastador","daño":(fuerza_total*2)*3},"ultimate":{"nombre":"Técnica del dragón","daño":fuerza_total + defensa_total_mon}},
    "Nigromante":{"basico":{"nombre":"Toque oscuro","daño":magia_total},"principal":{"nombre":"Maldición de decadencia","daño":magia_total,"debuffo":[fuerza_total_mon - (fuerza_total_mon//3),defensa_total_mon - (defensa_total_mon//3)]},"ultimate":{"nombre":"Rito de aniquilación","daño":magia_total - (defensa_total_mon - 50)}}
}
#--------------------DICCIONARIOS--------------------
"""
CLASES
"""
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
"""
HEROES
"""
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
"""
ARMAS
"""
armas = {
    1:{"clase":1,"nombre":"Escudo Pesado","características":{"fuerza":1,"defensa":6},"debuffo":{"agilidad":-2}},
    2:{"clase":2,"nombre":"Espada Larga","características":{"fuerza":4,"agilidad":2}},
    3:{"clase":3,"nombre":"Dagas","características":{"fuerza":2,"agilidad":4}},
    4:{"clase":4,"nombre":"Cuchillos de Caza","características":{"fuerza":3,"agilidad":3}},
    5:{"clase":5,"nombre":"Baston Magico","características":{"magia":5,"defensa":1}},
    6:{"clase":6,"nombre":"Stigma Sagrado","características":{"magia":4,"defensa":2},"debuffo":{"vida": -2}},
    7:{"clase":7,"nombre":"Totem","características":{"fuerza":2,"defensa":4}},
    8:{"clase":8,"nombre":"Laúd","características":{"defensa":2,"agilidad":4}},
    9:{"clase":9,"nombre":"Nudilleras","características":{"fuerza":2,"magia":4}},
    10:{"clase":10,"nombre":"Baston Oscuro","características":{"magia":1,"defensa":5},"debuffo":{"vida": -3}}
}

"""
MONSTRUOS
"""
monstruos_debiles = {
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

#--------------------MENUS--------------------
#--------------------Menu0 --------------------
menu0 = {"cabezera":"Dragones y Mazmorras",
    "opciones": ["Jugar",
    "Crear",
    "Editar",
    "Listar",
    "Salir"]}

#--------------------Menu2--------------------
menu2 = {"cabezera":"Menu de creacion",
    "opciones": ["Crear personaje",
    "Crear arma",
    "Volver"]}

"""
PARTE PERSONAJE
"""
#Para eleccionar su clase/arma/estadisticas
eleccion_clase = {"cabezera":"Eleccion de clase",
                  "opciones":[]}

eleccion_arma = {"cabezera":"Eleccion de arma",
                  "opciones":[]}

eleccion_estadisticas = {"cabezera":"Selecciona una estadistica",
    "opciones": ["Fuerza",
    "Magia",
    "Defensa",
    "Agilidad",
    "Vida"]}

#Para mostrar
nuevo_personaje = "Nuevo personaje".center(40,"=") + "\n"

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

"""
PARTE ARMA
"""
#Seleccion de clase
clase_nueva_arma = {"cabezera":"Clase nueva arma",
              "opciones":[]}

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
menu3 = {"cabezera":"Menu de editar",
    "opciones": ["Editar personaje",
    "Editar arma",
    "Volver"]}

#Seleccionar
menu_personaje = {"cabezera":"Selecciona personaje",
                  "opciones":[]}

arma_seleccion = {"cabezera":"Editar {}",
    "opciones": ["Nombre",
    "Salir"]}

pers_seleccion = {"cabezera":"Editar {}",
    "opciones": ["Nombre",
    "Cambiar arma",
    "Salir"]}

#--------------------Menu4--------------------
menu4 = {"cabezera":"Listas",
    "opciones": ["Lista personajes",
    "Lista armas",
    "Monstruos",
    "Volver"]}


#Menu de listar personajes
listar_personajes = {"cabezera":"Listar personajes",
                     "opciones":["1) Listar por ID",
                                 "2) Listar por nombre",
                                 "3) Listar por fuerza",
                                 "4) Listar por magia",
                                 "5) Listar por defensa",
                                 "6) Listar por agilidad",
                                 "7) Listar por vida",
                                 "8) Volver"]}

listar_armas = {"cabezera":"Listar armas",
                     "opciones":["1) Listar por ID",
                                 "2) Listar por  nombre",
                                 "3) Listar por característica fuerza",
                                 "4) Listar por característica magia",
                                 "5) Listar por característica defensa",
                                 "6) Listar por característica agilidad",
                                 "7) Volver"]}

menu_lista_monstruos = {"cabezera":"Listas monstruos",
    "opciones": ["Monstruos debiles",
    "Monstruos bestia",
    "Monstruos humanoides",
    "Criaturas magicas",
    "Jefes",
    "Volver"]}

empezar_a_jugar = "Selecciona un heroe".center(50,"*") + "\n"

#JUEGO
print_piso = "Ronda {}".center(50,"=") + "\n"
seleccionar_heroe = "Has seleccionado al heroe {}."
info_turno = "Turno {}".center(50,"=") + "\n" +\
    "1) Bàsico: {}" + "\n" + \
    "2) Habilidad: {}" + "\n" + \
    "3) Ultimate: {}" + "\n"
atacas = "A {} le has hecho {} de daño, le quedan {} puntos de vida."
atacan = "El {} te ha hecho {} de daño, te quedan {} puntos de vida."
    

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

en_cooldown = "Aun no puedes utilizar esta habilidad."
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
