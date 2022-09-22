from Clase_4.data_stark import lista_personajes


    # "nombre": "Deadpool",
    # "identidad": "Wade Wilson",
    # "empresa": "Marvel Comics",
    # "altura": "188.0",
    # "peso": "95.319999999999993",
    # "genero": "M",
    # "color_ojos": "Brown",
    # "color_pelo": "No Hair",
    # "fuerza": "35",
    # "inteligencia": "good"

def stark_normalizar_datos(lista:list, clave:str) ->dict:
    '''
    Recorrer la lista y convertir al tipo de dato correcto las keys (solo con las keys que representan datos numéricos)

    Validar primero que el tipo de dato no sea del tipo al cual será casteado. 

    Si al menos un dato fue modificado, la función deberá imprimir como mensaje ‘Datos normalizados’, 
    caso contrario no imprimirá nada.
    
    Validar que la lista de héroes no esté vacía para realizar sus acciones, 
    caso contrario imprimirá el mensaje: “Error: Lista de héroes vacía”

    '''

    retorno = "Error: Lista de héroes vacía"
    if type(lista) == type([]) and len(lista) > 0 and type(clave) == type(""):
        for caracteristica in lista_personajes:
            if type(caracteristica[clave]) == type(""):
                if clave == "altura":
                    caracteristica["altura"] = float(caracteristica["altura"])
                elif clave == "peso":
                    caracteristica["peso"] = float(caracteristica["peso"])
                elif clave == "fuerza":
                    caracteristica["fuerza"] = int(caracteristica["fuerza"])
        retorno = "Datos normalizados"
    return retorno

stark_normalizar_datos(lista_personajes,"peso")
# print(lista_personajes)

def obtener_nombre (diccionario:dict) -> str:

    '''
    recibirá por parámetro un diccionario el cual representara a un héroe 
    y devolverá un string el cual contenga su nombre formateado de la siguiente manera: 

    Nombre: Howard the Duck

    '''

    if type(diccionario) == type({}) and len(diccionario) > 0 :
        retorno = print("nombre : {0}".format(diccionario["nombre"]))
    return retorno

# obtener_nombre(lista_personajes[5])

def imprimir_dato(dato:str):

    '''
    recibirá por parámetro un string y deberá imprimirlo en la consola. La función no tendrá retorno.
    '''
    print(dato)

#imprimir_dato(lista_personajes)


def stark_imprimir_nombres_heroes(lista:str):

    '''
    recibirá por parámetro la lista de héroes y deberá imprimirla en la consola.
    '''
    retorno = 0
    if type(lista) == type([]) and len(lista) > 0 :
        for heroe in lista_personajes:
            retorno = imprimir_dato(obtener_nombre, heroe["nombre"])
    return retorno

stark_imprimir_nombres_heroes(lista_personajes["nombre"])
print(lista_personajes)

