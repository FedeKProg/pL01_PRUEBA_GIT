lista = [1,9,4,6,5,7,3,2,8]

def buscar_minimo(lista_busqueda:list)->list:
    minimo = 0
    for i in range(len(lista_busqueda)):
        if lista_busqueda[i] < lista_busqueda[minimo]:
            minimo = i
    return minimo

#print(buscar_minimo(lista))

def lista_de_fede(lista_resultado:list)->list:
    lista_original = lista_resultado.copy()
    lista_resultado = []

    while len(lista_original) > 0:
        minimo = buscar_minimo(lista_original)
        lista_resultado.append(lista_original.pop(minimo))

    return lista_resultado

lista_resultado = lista_de_fede(lista)

print(lista)
print(lista_resultado)

