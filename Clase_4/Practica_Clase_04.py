from data_stark import lista_personajes

''''
for heroe in lista_personajes:
    if heroe["genero"] == "M":
        print(heroe["nombre"])

for heroe in lista_personajes:
    if heroe["genero"] == "F":
        print(heroe["nombre"])
'''

def heroina_mas_alta():
    heroe_alto = lista_personajes[0]
    heroe = float(heroe_alto["altura"])
    for heroe in lista_personajes:
        heroe["altura"] = float(heroe["altura"])
        if (heroe["genero"] == "F" and heroe["altura"] >= heroe_alto["altura"]):
            heroe_alto = heroe
    print("La heroina con la mayor altura es : {0}, con una altura de {1}".format(heroe_alto["nombre"], heroe_alto["altura"]))

def heroe_mas_alto():
    heroe_alto = lista_personajes[0]
    heroe = float(heroe_alto["altura"])
    for heroe in lista_personajes:
        heroe["altura"] = float(heroe["altura"])
        if (heroe["genero"] == "M" and heroe["altura"] >= heroe_alto["altura"]):
            heroe_alto = heroe
    print("El heroe con la mayor altura es : {0}, con una altura de {1}".format(heroe_alto["nombre"], heroe_alto["altura"]))

def heroina_mas_baja():
    heroe_bajo = lista_personajes[0]
    heroe = float(heroe_bajo["altura"])
    for heroe in lista_personajes:
        heroe["altura"] = float(heroe["altura"])
        if (heroe["genero"] == "F" and heroe["altura"] >= heroe_bajo["altura"]):
            heroe_bajo = heroe
    print("La heroina con la menor altura es : {0}, con una altura de {1}".format(heroe_bajo["nombre"], heroe_bajo["altura"]))

def heroe_mas_bajo():
    heroe_bajo = lista_personajes[0]
    heroe = float(heroe_bajo["altura"])
    for heroe in lista_personajes:
        heroe["altura"] = float(heroe["altura"])
        if (heroe["genero"] == "M" and heroe["altura"] <= heroe_bajo["altura"]):
            heroe_bajo = heroe
    print("El heroe con la menor altura es : {0}, con una altura de {1}".format(heroe_bajo["nombre"], heroe_bajo["altura"]))

def Promedio_Heroes():
    acumulador_altura = 0
    contador_heroes = 0
    Promedio_Altura_F = lista_personajes [0]
    heroe = float(Promedio_Altura_F["altura"])
    for heroe in lista_personajes:
            if (heroe["genero"] == "F"):
                contador_heroes += 1
                acumulador_altura += float(heroe["altura"])
    promedio_altura = acumulador_altura  / contador_heroes
    print("El promedio de altura de los heroes es : {0}".format(promedio_altura))

def Promedio_Heroinas():
    acumulador_altura = 0
    contador_heroes = 0
    Promedio_Altura_M = lista_personajes [0]
    heroe = float(Promedio_Altura_M["altura"])
    for heroe in lista_personajes:
            if (heroe["genero"] == "M"):
                contador_heroes += 1
                acumulador_altura += float(heroe["altura"])
    promedio_altura = acumulador_altura  / contador_heroes
    print("El promedio de altura de los heroes es : {0}".format(promedio_altura))

def cantidad_personajes_por_color_ojos():
    #Determinar cuántos superhéroes tienen cada tipo de color de ojos.
    cantidad_personajes_por_color_ojos = {}

    for personaje in lista_personajes:
            cantidad_personajes_por_color_ojos[personaje["color_ojos"]] = 0

    for personaje in lista_personajes:
            cantidad_personajes_por_color_ojos[personaje["color_ojos"]] += 1

    for tipo in cantidad_personajes_por_color_ojos:
            print("existen {0} personajes con color de ojo {1}".format(cantidad_personajes_por_color_ojos[tipo],tipo ))

def cantidad_personajes_por_color_pelo():
    #K) Determinar cuántos superhéroes tienen cada tipo de color de pelo.
    cantidad_personajes_por_color_pelo = {}


    for personaje in lista_personajes:
        cantidad_personajes_por_color_pelo[personaje["color_pelo"]] = 0

    for personaje in lista_personajes:
        cantidad_personajes_por_color_pelo[personaje["color_pelo"]] += 1
    
    for tipo in cantidad_personajes_por_color_pelo:
        print("existen {0} personajes con color de pelo {1}".format(cantidad_personajes_por_color_pelo[tipo],tipo ))

def cuantos_por_tipo_de_inteligencia():
    #Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).
    tipo_inteligencia = {}

    for personaje in lista_personajes:
        tipo_inteligencia[personaje["inteligencia"]] = 0

    for personaje in lista_personajes:
        tipo_inteligencia[personaje["inteligencia"]] += 1
    
    for tipo in tipo_inteligencia:
        print("existen {0} personajes de inteligencia {1}".format(tipo_inteligencia[tipo],tipo ))


def lista_color_ojos():
    
    dict_color_ojos = {}

    for personajes in lista_personajes:
            color_ojos_normalizar = personajes["color_ojos"].lower()
            dict_color_ojos[color_ojos_normalizar] = []
        
    for personajes in lista_personajes:
            for color in dict_color_ojos:
                color_normalizar = color.lower()
                if personajes["color_ojos"].lower() == color_normalizar:
                    dict_color_ojos[color_normalizar].append(personajes["nombre"])
    print(dict_color_ojos)

def lista_color_pelo():

    dict_color_pelo = {}
    for personajes in lista_personajes:
            color_pelo_normalizar = personajes["color_pelo"].lower()
            dict_color_pelo[color_pelo_normalizar] = []
        
    for personajes in lista_personajes:
            for color in dict_color_pelo:
                color_normalizar = color.lower()
                if personajes["color_pelo"].lower() == color_normalizar:
                    dict_color_pelo[color_normalizar].append(personajes["nombre"])
    print(dict_color_pelo)

def lista_inteligencia():
    dict_inteligencia = {}
    for personajes in lista_personajes:
                inteligencia_normalizar = personajes["inteligencia"].lower()
                dict_inteligencia[inteligencia_normalizar] = []
            
    for personajes in lista_personajes:
                for inteligencia in dict_inteligencia:
                    color_normalizar = inteligencia.lower()
                    if personajes["inteligencia"].lower() == inteligencia_normalizar:
                        dict_inteligencia[color_normalizar].append(personajes["nombre"])
    print(dict_inteligencia)

while True:

   
    respuesta = input("\nElija una de las siguientes opciones: \n" 
                        "1- altura del heroe mas alto \n" 
                        "2- altura de la heroina mas alta \n" 
                        "3- altura del heroe mas bajo \n" 
                        "4- altura de la heroina mas baja \n" 
                        "5- altura promedio de los heroes \n"
                        "6- altura promedio de las heroinas \n"
                        "7- cantidad de heroes por color de ojos \n"
                        "8- cantidad de heroes por color de pelo \n" 
                        "9- cantidad de heroes por inteligencia \n"
                        "10- lista de heroes por color de ojos \n" 
                        "11- lista de heroes por color de ojos \n" 
                        "12- lista de heroes por color de ojos \n" 
                        "13- salir\n\n")
    if(respuesta == "1"): 
        heroe_mas_alto()
    elif(respuesta == "2"):
        heroina_mas_alta()
    elif(respuesta == "3"):
        heroe_mas_bajo()
    elif(respuesta == "4"):
        heroina_mas_baja()
    elif(respuesta == "5"):
        Promedio_Heroes()
    elif(respuesta == "6"):
        Promedio_Heroinas()
    elif(respuesta == "7"):
        cantidad_personajes_por_color_ojos()
    elif(respuesta == "8"):
        cantidad_personajes_por_color_pelo()
    elif(respuesta == "9"):
        cuantos_por_tipo_de_inteligencia()
    elif(respuesta == "10"):
        lista_color_ojos()
    elif(respuesta == "11"):
        lista_color_pelo()
    elif(respuesta == "12"):
        lista_inteligencia()
    elif(respuesta == "13"):
        break