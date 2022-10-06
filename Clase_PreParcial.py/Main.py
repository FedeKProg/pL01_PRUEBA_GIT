'''
1- Listar X cantidad de heroes
2- Lista de heroe por altura (High and Low)
3- Lista de heroe por peso (High and Low)
4- Promedio de cualquier key numerica, y lsita de quienes superan o no el promedio
5- Lista heroes por inteligencia
6- Exportar por csv
7- Salir
'''
import re
import Calculos 
from Calculos import lista_heroes

url_archivo = r"C:\Users\Freelancer\Desktop\pL01_Ejercicios\pL01_PRUEBA_GIT\Clase_PreParcial.py\data_stark (2).json"


def menu_principal():
    contenido = []
    while True:

        respuesta = input("\nElija una de las siguientes opciones: \n" 
                                "1- Listar X cantidad de heroes \n" 
                                "2- Lista de heroe por altura (High and Low) \n" 
                                "3- Lista de heroe por peso (High and Low) \n" 
                                "4- Promedio de cualquier key numerica, y lsita de quienes superan o no el promedio \n" 
                                "5- Lista heroes por inteligencia \n"
                                "6- Exportar por csv la lista elegida (del 1 al 4 de las opciones) \n"
                                "7- Salir \n\n")
        lista_heroes = Calculos.abrir_json(url_archivo)

        if(respuesta == "1"): 
            contenido = Calculos.listado_heroes(lista_heroes)
        elif(respuesta == "2"):
            orden_lista = input("Ingrese com odesea ordenar la lista. \n"
						"asc- para ascendente \n"
	 					"dsc- para descendente \n\n")
            validar_respuesta = Calculos.validar_respuesta(orden_lista, "asc|dsc")
            if(validar_respuesta != False):
                contenido = Calculos.mostrar(Calculos.lista_ordenada_altura(lista_heroes,orden_lista))
            else:
                print("Error. Ingrese nuevamente\n")
                continue
        elif(respuesta == "3"):
            orden_lista = input("Ingrese com odesea ordenar la lista. \n"
						"asc- para ascendente \n"
	 					"dsc- para descendente \n\n")
            validar_respuesta = Calculos.validar_respuesta(orden_lista, "asc|dsc")
            if(validar_respuesta != False):
                contenido = Calculos.mostrar(Calculos.lista_ordenada_fuerza(lista_heroes,orden_lista))
            else:
                print("Error. Ingrese nuevamente\n")
                continue
        elif(respuesta == "4"):
            elemento = input("Seleccione el atributo que desea listar\n"
                            "altura\n"
                            "fuerza\n"
                            "peso\n")
            validar_respuesta = Calculos.validar_respuesta(elemento, "altura|fuerza|peso")
            if(validar_respuesta != False):                
                condicion = input("Ingrese si desea ver la lista de mayor o menor \n")
                validar_respuesta = Calculos.validar_respuesta(condicion, "mayor|menor")
                if(validar_respuesta != False):   
                    contenido = Calculos.mostrar(Calculos.calcular_promedio_keys(lista_heroes,elemento,condicion))
                else:
                    print("Error. Ingrese nuevamente\n")
                    continue
            else:
                print("Error. Ingrese nuevamente\n")
                continue
        elif(respuesta == "5"):
            patron = input("Seleccione la lista de que tipo de inteligencia desea ver: \n"
                                    "good \n"
                                    "average \n"
                                    "high \n\n")
            validar_respuesta = Calculos.validar_respuesta(patron, "good|average|high")
            if(validar_respuesta != False):   
                Calculos.listado_inteligencia(lista_heroes,patron)
            else:
                print("Intelgencia elegida no disponible \n")
                continue
        elif(respuesta == "6"):
            Calculos.export_to_csv(str(contenido),"data_stark.csv")
        elif(respuesta == "7"):
            break
menu_principal()