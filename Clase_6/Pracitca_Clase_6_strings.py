from data_stark import lista_personajes
'''
{
   "nombre": "Howard the Duck",
   "identidad": "Howard (Last name unrevealed)",
   "empresa": "Marvel Comics",
   "altura": "79.349999999999994",
   "peso": "18.449999999999999",
   "genero": "M",
   "color_ojos": "Brown",
   "color_pelo": "Yellow",
   "fuerza": "2",
   "inteligencia": "average"
 }

'''

def extraer_iniciales(nombre_personaje:str) -> str:

    '''
    La función deberá devolver a partir del parámetro recibido un nuevo string con las iniciales del nombre del personaje 
    seguidos por un punto (.)

    Ejemplo de la salida de la función para Howard the Duck:
    H.D.

    '''
    retorno = "N/A"
    iniciales = " "

    if type(nombre_personaje) == type(str()) and len(nombre_personaje) > 0:
        nombre_personaje = nombre_personaje.upper()
        nombre_personaje = nombre_personaje.replace("THE ", "")
        nombre_personaje = nombre_personaje.replace("-", "")
        iniciales_personajes = nombre_personaje.split(" ")
        for inicial in iniciales_personajes:
            iniciales += inicial[0] + "."
        
        retorno = iniciales
    return retorno


# for heroe in lista_personajes:
#     print(extraer_iniciales(heroe["nombre"]))

def definir_iniciales_nombre(heroe:dict):
    '''
    La función deberá agregar una nueva clave al diccionario recibido como parámetro. 
    La clave se deberá llamar ‘iniciales’ y su valor será el obtenido de llamar a la función ‘extraer_iniciales’

    '''
    retorno = False
    if type(heroe) == type (dict()):
        for clave in heroe:
            if clave == "nombre":
                heroe["iniciales"] = extraer_iniciales(heroe["nombre"])
                retorno = True
                break
    print(heroe)
    return retorno

# for heroe in lista_personajes:
#     print(definir_iniciales_nombre(heroe))

def agregar_iniciales_nombre(lista_heroes:list):

    retorno = "El origen de datos no contiene el formato correcto"
    if type(lista_heroes) == type(list()) and len(lista_heroes) > 1: 
        for heroe in lista_personajes:
            definir_iniciales_nombre(heroe)
            retorno = True
        else:
            retorno = False
            print("El origen de datos no contiene el formato correcto")
    print(heroe)
    return retorno

# agregar_iniciales_nombre(lista_personajes)

def stark_imprimir_nombres_con_iniciales(lista_heroes:list):
    '''
    La función deberá utilizar la función agregar_iniciales_nombre’ 
    para añadirle las iniciales a los diccionarios contenidos en la lista_heroes
    Luego deberá imprimir la lista completa de los nombres de los personajes 
    seguido de las iniciales encerradas entre paréntesis () 
    Ejemplo de salida:
    * Howard the Duck (H.D.)
    * Rocket Raccoon (R.R.)

    '''
    lista_iniciales = []
    if type(lista_heroes) == type(list()) and len(lista_heroes) > 1: 
        for heroe in lista_heroes:
            agregar_iniciales_nombre(lista_heroes)
            nombre_e_iniciales ="* {0} ({1})".format(heroe["nombre"],heroe["iniciales"])
            lista_iniciales.append(nombre_e_iniciales)
        for nombre_e_iniciales in lista_iniciales:
            print(nombre_e_iniciales)


stark_imprimir_nombres_con_iniciales(lista_personajes)