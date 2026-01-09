from Funciones_Rol.Variables_del_proyecto import  *

def editar_nombre(opc,lista,dic):
    nombre = dic[lista[opc - 1]]["nombre"]
    nuevo_nombre = input("Nuevo nombre:\n")
    while not nuevo_nombre.replace(" ","").isalpha():
        print(formato_invalido_letras)
        input("Enter to continue")
        nuevo_nombre = input("Nuevo nombre:\n")
    print("El nombre: {}\nHa combiado por: {}".format(nombre, nuevo_nombre))
    input("Enter para continuar")
    dic[lista[opc - 1]]["nombre"] = nuevo_nombre
    return dic

def ordenar_y_generar_opciones(data_dict, eleccion):
    keys = list(data_dict.keys())

    for pasada in range(len(keys)):
        cambios = False
        for i in range(len(keys) - 1 - pasada):
            if data_dict[keys[i]]["nombre"].upper() > data_dict[keys[i + 1]]["nombre"].upper():
                cambios = True
                aux = keys[i]
                keys[i] = keys[i + 1]
                keys[i + 1] = aux
        if not cambios:
            break

    eleccion["opciones"] = []
    for i in range(len(keys)):
        eleccion["opciones"].append(data_dict[keys[i]]["nombre"])
    eleccion["opciones"].append("Salir")

    return keys
