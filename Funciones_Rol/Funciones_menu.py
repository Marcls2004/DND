def gen_menu(menu):
    cabezera = menu["cabezera"].center(40,"=") + "\n"
    datos = ""
    resultado = ""
    for i in range(len(menu["opciones"])):
        datos += str(i + 1) + ") " +  menu["opciones"][i] + "\n"
    return cabezera + datos


#sirve para menus que pueden tener diferentes nombres.
def gen_menu_2(menu, nombre):
    cabezera = menu["cabezera"].format(nombre).center(40, "=") + "\n"
    datos = ""
    for i in range(len(menu["opciones"])):
        datos += str(i + 1) + ") " + menu["opciones"][i] + "\n"
    return cabezera + datos

def menu(tupla):
    texto = ""
    for i in range(len((tupla))):
        texto += str(i+1)+")"+ tupla[i] + "\n"
    while True:
        print(texto)
        opc = input("Option:")
        if not opc.isdigit():
            print("Only Numeric Options")
        elif opc in range(1, len(tupla) + 1):
            print("Option Out Of range")
        else:
            opc = int(opc)
            return opc 