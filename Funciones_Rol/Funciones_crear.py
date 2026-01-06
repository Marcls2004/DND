def burbuja(lista,metodo):
    for pasada in range(len(lista)):
        cambios = False
        for i in range(len(lista)-1-pasada):
            if metodo[lista[i]] > metodo[lista[i+1]]:
                cambios = True
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
        if not cambios:
            break
    return lista