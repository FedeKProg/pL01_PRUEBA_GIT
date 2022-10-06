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

def lista_2_fede(lista_ordenada:list)->list:
    lista_desorden = lista_ordenada.copy()
    flag = True
    tope = 1
    while flag == True:
        flag = False
        for i in range(len(lista_desorden)-tope):
            if lista_desorden[i] > lista_desorden[i+1]:
                backup = lista_desorden[i]
                lista_desorden[i] = lista_desorden[i+1]
                lista_desorden[i+1] = backup
                flag = True
    tope += 1
    return lista_desorden

lista_desorden = lista_2_fede(lista)
print(lista_desorden)

def lista_pivot(lista_para_ordenar:list)->list:
    lista_original = lista_para_ordenar.copy()
    lista_de = []
    lista_iz = []
    if len(lista_para_ordenar) <= 1:
        return lista_para_ordenar
    else:
        pivot = lista_para_ordenar[0]
        for elemento in lista_original[1:]:
            if elemento > pivot:
                lista_de.append(elemento)
            else:
                lista_iz.append(elemento)
    lista_iz = lista_pivot(lista_iz)
    lista_iz.append(pivot)
    lista_de = lista_pivot(lista_de)
    return lista_iz + lista_de

lista_original = lista_pivot(lista)
print(lista_original)

