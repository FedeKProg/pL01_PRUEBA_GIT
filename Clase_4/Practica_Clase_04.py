from Clase_4.data_stark import lista_personajes

''''
for heroe in lista_personajes:
    if heroe["genero"] == "M":
        print(heroe["nombre"])

for heroe in lista_personajes:
    if heroe["genero"] == "F":
        print(heroe["nombre"])
'''

# def heroina_mas_alta():
#     heroe_alto = lista_personajes[0]
#     heroe = float(heroe_alto["altura"])
#     for heroe in lista_personajes:
#         heroe["altura"] = float(heroe["altura"])
#         if (heroe["genero"] == "F" and heroe["altura"] >= heroe_alto["altura"]):
#             heroe_alto = heroe
#     print("La heroina con la mayor altura es : {0}, con una altura de {1}".format(heroe_alto["nombre"], heroe_alto["altura"]))

# def heroe_mas_alto():
#     heroe_alto = lista_personajes[0]
#     heroe = float(heroe_alto["altura"])
#     for heroe in lista_personajes:
#         heroe["altura"] = float(heroe["altura"])
#         if (heroe["genero"] == "M" and heroe["altura"] >= heroe_alto["altura"]):
#             heroe_alto = heroe
#     print("El heroe con la mayor altura es : {0}, con una altura de {1}".format(heroe_alto["nombre"], heroe_alto["altura"]))

# def heroina_mas_baja():
#     heroe_bajo = lista_personajes[0]
#     heroe = float(heroe_alto["altura"])
#     for heroe in lista_personajes:
#         heroe["altura"] = float(heroe["altura"])
#         if (heroe["genero"] == "F" and heroe["altura"] <= heroe_alto["altura"]):
#             heroe_alto = heroe
#     print("La heroina con la menor altura es : {0}, con una altura de {1}".format(heroe_alto["nombre"], heroe_alto["altura"]))

# def heroe_mas_bajo():
#     heroe_bajo = lista_personajes[0]
#     heroe = float(heroe_alto["altura"])
#     for heroe in lista_personajes:
#         heroe["altura"] = float(heroe["altura"])
#         if (heroe["genero"] == "M" and heroe["altura"] <= heroe_alto["altura"]):
#             heroe_alto = heroe
#     print("El heroe con la menor altura es : {0}, con una altura de {1}".format(heroe_alto["nombre"], heroe_alto["altura"]))

# def Promedio_Heroes():
#     acumulador_altura = 0
#     contador_heroes = 0
#     Promedio_Altura_F = lista_personajes [0]
#     heroe = float(Promedio_Altura_F["altura"])
#     for heroe in lista_personajes:
#             if (heroe["genero"] == "F"):
#                 contador_heroes += 1
#                 acumulador_altura += float(heroe["altura"])
#     promedio_altura = acumulador_altura  / contador_heroes
#     print("El promedio de altura de los heroes es : {0}".format(promedio_altura))

# def Promedio_Heroinas():
#     acumulador_altura = 0
#     contador_heroes = 0
#     Promedio_Altura_M = lista_personajes [0]
#     heroe = float(Promedio_Altura_M["altura"])
#     for heroe in lista_personajes:
#             if (heroe["genero"] == "M"):
#                 contador_heroes += 1
#                 acumulador_altura += float(heroe["altura"])
#     promedio_altura = acumulador_altura  / contador_heroes
#     print("El promedio de altura de los heroes es : {0}".format(promedio_altura))



#def lista_color_ojos():
    
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

