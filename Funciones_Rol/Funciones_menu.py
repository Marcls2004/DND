def gen_menu(menu):
    cabezera = menu["cabezera"].center(40,"=") + "\n"
    datos = ""
    for i in range(len(menu["opciones"])):
        datos += str(i + 1) + ") " +  menu["opciones"][i] + "\n"
    return cabezera + datos

