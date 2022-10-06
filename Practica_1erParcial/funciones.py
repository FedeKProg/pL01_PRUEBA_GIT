import json
import re

'''
{
			"id": 1,
			"nombre": "bulbasaur",
			"tipo": ["planta"],
			"evoluciones": ["ivysaur", "venusaur"],
			"poder": 4,
			"fortaleza":["agua"],
			"debilidad":["fuego"]
		},
'''

url_archivo = r"C:\Users\Freelancer\Desktop\pL01_Ejercicios\pL01_PRUEBA_GIT\Practica_1erParcial\pokedex.json"

def abrir_json(path:str)->list:
	with open(path, "r") as file:
		datos_pokemones = json.load(file)
	return datos_pokemones["pokemones"]
# print(abrir_json(url_archivo))
lista_pokemones = abrir_json(url_archivo)

def validar_entero(numero_str: str) -> int:
	result = re.match("^[0-9]+$", numero_str)
	if result != None:
		return int(numero_str)
	else:
		False

def listado_pokemones(lista_pokemones: list):
	'''
	Recibe: recibe la lista extraida del archivo json.

	Devuelve: La lista con la cantidad de elementos elegido por el usuario.

	Valida: Se valida que no supere el maximo de la lista.

	'''

	cant_pokemones = (input("Ingrese la cantidad de pokemones a listar: \n"))
	cant_pokemones = validar_entero(cant_pokemones)
	if cant_pokemones != False:
		if cant_pokemones > len(lista_pokemones):
			print("La cantidad ingresada no es valida, ingrese nuevamente: \n")
		else:
			for i in range(cant_pokemones):
				print(lista_pokemones[i])
	else:
		print("El caracter ingresado no es valido")
# listado_pokemones(lista_pokemones)

def buscar_minimo(lista_pokemones: list,clave:str) -> int:
	minimo = 0
	for i in range(len(lista_pokemones)):
		if lista_pokemones[i][clave] < lista_pokemones[minimo][clave]:
			minimo = i
	return minimo

def buscar_maximo(lista_pokemones:list,clave:str) -> int:
	maximo = 0
	for i in range(len(lista_pokemones)):
		if lista_pokemones[i][clave] > lista_pokemones[maximo][clave]:
			maximo = i
	return maximo

def lista_ordenada_poder(lista_pokemones: list,orden_lista:str) -> list:
	'''
	Ordenar y Listar héroes por altura.
	Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’)
	'''
	# orden_lista = input("Ingrese com odesea ordenar la lista. \n"
	# 					"asc- para ascendente \n"
	#  					"dsc- para descendente \n\n")
	validar = re.search('asc|desc', orden_lista, re.IGNORECASE)
	orden_lista = orden_lista.lower()

	copia_lista_pokemones = lista_pokemones.copy()
	lista_pokemones_ordenenada = []

	while len(copia_lista_pokemones) > 0:
		if orden_lista == "asc":
			minimo = buscar_minimo(copia_lista_pokemones, "poder")
			lista_pokemones_ordenenada.append(copia_lista_pokemones.pop(minimo))
		elif orden_lista == "dsc":
			maximo = buscar_maximo(copia_lista_pokemones, "poder")
			lista_pokemones_ordenenada.append(copia_lista_pokemones.pop(maximo))
		else:
			print("Valor ingresado no valido")
	for pokemon in lista_pokemones_ordenenada:
		print(pokemon["nombre"],pokemon["poder"])
	return lista_pokemones_ordenenada

# lista_ordenada_poder(lista_pokemones,"dsc")

def lista_ordenada_ID(lista_pokemones: list,orden_lista:str) -> list:
	'''
	Ordenar y Listar héroes por altura.
	Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’)
	'''
	# orden_lista = input("Ingrese com odesea ordenar la lista. \n"
	# 					"asc- para ascendente \n"
	#  					"dsc- para descendente \n\n")
	validar = re.search('asc|desc', orden_lista, re.IGNORECASE)
	orden_lista = orden_lista.lower()

	copia_lista_pokemones = lista_pokemones.copy()
	lista_pokemones_ordenenada = []

	while len(copia_lista_pokemones) > 0:
		if orden_lista == "asc":
			minimo = buscar_minimo(copia_lista_pokemones, "id")
			lista_pokemones_ordenenada.append(copia_lista_pokemones.pop(minimo))
		elif orden_lista == "dsc":
			maximo = buscar_maximo(copia_lista_pokemones, "id")
			lista_pokemones_ordenenada.append(copia_lista_pokemones.pop(maximo))
		else:
			print("Valor ingresado no valido")
	for pokemon in lista_pokemones_ordenenada:
		print(pokemon["nombre"],pokemon["id"])
	return lista_pokemones_ordenenada

#lista_ordenada_ID(lista_pokemones,"asc")

def calcular_promedio_keys(lista_pokemones:list, key:str, condicion:str)-> list:
	'''
	Recibe: recibe la lista extraida del archivo json.

	Devuelve: La lista con el promedio de la key y la lista que compla con el requerimiento elegido por el usuatio(mayor o menor)

	Valida: Se valida que no supere el maximo de la lista.
	'''
	cantidad_pokemones = len(lista_pokemones)
	acumulador_keys = 0
	lista_condicion = []

	for pokemon in lista_pokemones:
		acumulador_keys += len(pokemon[key])
	promedio_keys = acumulador_keys / cantidad_pokemones
	print("El promedio es: {0}".format(promedio_keys))
	for pokemon in lista_pokemones:
		if condicion == "menor"and len(pokemon[key]) < promedio_keys:
				lista_condicion.append(pokemon)
		elif condicion == "mayor"and len(pokemon[key]) > promedio_keys:
				lista_condicion.append(pokemon)
	print(lista_condicion)
	return lista_condicion

# print(calcular_promedio_keys(lista_pokemones, "tipo","mayor"))

def listado_tipo(lista_pokemones:list,patron:str)->list:
	'''
	Recibe: la lista extraido por json

	Buscar héroes por inteligencia [fuego, volador, electrico, piedra, fantasma, veneno, hielo, psiquico, lucha, acero, agua]
	y listar en consola los que cumplan dicha búsqueda.
	'''

	for pokemon in lista_pokemones:
		if re.search(patron,pokemon["tipo"],re.IGNORECASE):
			print("{0} - {1}".format(pokemon["nombre"], pokemon["tipo"]))
	return 
#print(listado_tipo(lista_pokemones,"lucha"))

def mostrar(lista_pokemones:list):
	mensaje = ""

	for pokemones in lista_pokemones:
		mensaje += "{0}, {1}, {2}, {3}, {4}, {5}, {6} \n".format(pokemones["nombre"],pokemones["id"],pokemones["tipo"]
		,pokemones["evoluciones"],pokemones["poder"],pokemones["fortaleza"], pokemones["debilidad"])
	return mensaje
		
def export_to_csv(mensaje:str,nombre_archivo:str):
	'''Exportar a CSV la lista de héroes ordenada según opción elegida anteriormente [1-4]'''
	
	nombre_archivo = "data_pokedex.csv"
	with open(nombre_archivo, "w+") as archivo:
		archivo.write(mensaje)
