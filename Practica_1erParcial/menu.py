import re
import funciones 
from funciones import lista_pokemones

url_archivo = r"C:\Users\Freelancer\Desktop\pL01_Ejercicios\pL01_PRUEBA_GIT\Practica_1erParcial\pokedex.json"


def menu_principal():
    contenido = []
    while True:

        respuesta = input("\nElija una de las siguientes opciones: \n" 
                                "1- Listar X cantidad de pokemones \n" 
                                "2- Lista de heroe por poder (High and Low) \n" 
                                "3- Lista de heroe por ID (High and Low) \n" 
                                "4- Promedio de cualquier lista, y detalla de quienes superan o no el promedio \n" 
                                "5- Lista heroes por tipo \n"
                                "6- Exportar por csv la lista elegida (del 1 al 4 de las opciones) \n"
                                "7- Salir \n\n")
        lista_pokemones = funciones.abrir_json(url_archivo)

        if(respuesta == "1"): 
            contenido = funciones.listado_pokemones(lista_pokemones)
        elif(respuesta == "2"):
            orden_lista = input("Ingrese como desea ordenar la lista. \n"
						"asc- para ascendente \n"
	 					"dsc- para descendente \n\n")
            if(orden_lista == "asc" or orden_lista == "dsc"):
                contenido = funciones.mostrar(funciones.lista_ordenada_poder(lista_pokemones,orden_lista))
            else:
                print("Error. Ingrese nuevamente\n")
                continue
        elif(respuesta == "3"):
            orden_lista = input("Ingrese como desea ordenar la lista. \n"
						"asc- para ascendente \n"
	 					"dsc- para descendente \n\n")
            if(orden_lista == "asc" or orden_lista == "dsc"):
                contenido = funciones.mostrar(funciones.lista_ordenada_ID(lista_pokemones,orden_lista))
            else:
                print("Error. Ingrese nuevamente\n")
                continue
        elif(respuesta == "4"):
            elemento = input("Seleccione el atributo que desea listar\n"
                            "evoluciones\n"
                            "fortaleza\n"
                            "debilidad\n"
                            "tipo\n")
            if elemento == "evoluciones" or elemento == "fortaleza" or elemento == "debilidad" or elemento == "tipo":                
                condicion = input("Ingrese si desea ver la lista de mayor o menor \n")
                if (condicion == "mayor" or condicion =="menor"):
                    contenido = funciones.mostrar(funciones.calcular_promedio_keys(lista_pokemones,elemento,condicion))
                else:
                    print("Error. Ingrese nuevamente\n")
                    continue
            else:
                print("Error. Ingrese nuevamente\n")
                continue
        elif(respuesta == "5"):
            patron = input("Seleccione la lista de que tipo de inteligencia desea ver: \n"
                                    "fuego \n" 
                                    "volador \n"
                                    "electrico \n"
                                    "piedra \n"
                                    "fantasma \n"
                                    "veneno \n"
                                    "hielo \n"
                                    "psiquico \n"
                                    "lucha \n"
                                    "acero \n"
                                    "agua \n\n")
            funciones.listado_tipo(lista_pokemones,patron)
        elif(respuesta == "6"):
            funciones.export_to_csv(str(contenido),"data_pokedex.csv")
        elif(respuesta == "7"):
            break
menu_principal()