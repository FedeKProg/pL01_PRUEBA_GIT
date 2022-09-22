from Clase_4.data_stark import lista_personajes

'''
for heroe in lista_personajes:
    print(heroe["nombre"],heroe["altura"])


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


def heroe_mas_alto():

    heroe_alto = lista_personajes[0]
    heroe = float(heroe_alto["altura"])
    for heroe in lista_personajes:
        heroe["altura"] = float(heroe["altura"])
        if (heroe["altura"] > heroe_alto["altura"]):
            heroe_alto = heroe

    print("El heroe con la mayor altura es : {0}, con una altura de {1}".format(heroe_alto["nombre"], heroe_alto["altura"]))

def heroe_mas_bajo():

    heroe_bajo = lista_personajes[0]
    heroe = float(heroe_bajo["altura"])
    for heroe in lista_personajes:
        heroe["altura"] = float(heroe["altura"])
        if (heroe["altura"] <= heroe_bajo["altura"]):
            heroe_bajo =  heroe

    print("El heroe con la menor altura es : {0}, con una altura de {1}".format(heroe_bajo["nombre"], heroe_bajo["altura"]))

def promedio_altura():


    heroe_bajo = lista_personajes[0]
    heroe = float(heroe_bajo["altura"])
    for heroe in lista_personajes:
        acumulador_altura = 0
        contador_heroes = 0
        contador_heroes += 1
        acumulador_altura += heroe["altura"]
    promedio_altura = acumulador_altura  / contador_heroes
    print("El promedio de altura es : {0}".format(promedio_altura))

def heroe_mas_alto_nombre():

    heroe_alto = lista_personajes[0]
    heroe = float(heroe_alto["altura"])
    for heroe in lista_personajes:
        heroe["altura"] = float(heroe["altura"])
        if (heroe["altura"] > heroe_alto["altura"]):
            heroe_alto = heroe

    print("El heroe con la mayor altura es : {0}".format(heroe_alto["nombre"]))

def heroe_mas_bajo_nombre():

    heroe_bajo = lista_personajes[0]
    heroe = float(heroe_bajo["altura"])
    for heroe in lista_personajes:
        heroe["altura"] = float(heroe["altura"])
        if (heroe["altura"] <= heroe_bajo["altura"]):
            heroe_bajo =  heroe

    print("El heroe con la menor altura es : {0}".format(heroe_bajo["nombre"]))

def heroe_mas_pesado():
    heroe_mas_pesado = lista_personajes[0]
    heroe = float(heroe_mas_pesado["peso"])
    for heroe in lista_personajes:
        heroe["peso"] = float(heroe["peso"])
        if(heroe["peso"] > heroe_mas_pesado["peso"]):
            heroe_mas_pesado = heroe
    print("El heroe mas pesado es: {0}, con un peso de: {1}".format(heroe_mas_pesado["nombre"], heroe_mas_pesado["peso"]))

def heroe_menos_pesado():
    heroe_menos_pesado = lista_personajes[0]
    heroe = float(heroe_menos_pesado["peso"])
    for heroe in lista_personajes:
        heroe["peso"] = float(heroe["peso"])
        if(heroe["peso"] < heroe_menos_pesado["peso"]):
            heroe_menos_pesado = heroe
    print("El heroe menos pesado es: {0}, con un peso de: {1}".format(heroe_menos_pesado["nombre"], heroe_menos_pesado["peso"]))


while True:

   
    respuesta = input("\nElija una de las siguientes opciones: \n 1 para obtener la altura del heroe mas alto \n 2 para obtener la altura del heroe mas bajo \n 3 para obtener la altura promedio de los heroes \n 4 para obtener el nombre del heroe mas alto \n 5 para obtener el nombre del heroe mas bajo \n 6 para obtener el peso del heroe mas pesado \n 7 para obtener el peso del heroe mas liviano \n y 8 para salir\n\n")
    if(respuesta == "1"): 
        heroe_mas_alto()
    elif(respuesta == "2"):
        heroe_mas_bajo()
    elif(respuesta == "3"):
        promedio_altura()
    elif(respuesta == "4"):
        heroe_mas_alto_nombre()
    elif(respuesta == "5"):
        heroe_mas_bajo_nombre()
    elif(respuesta == "6"):
        heroe_mas_pesado()
    elif(respuesta == "7"):
        heroe_menos_pesado()
    elif(respuesta == "8"):
        break


