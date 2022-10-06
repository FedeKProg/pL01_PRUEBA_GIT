import json
import re



'''
 {
			"nombre": "Howard the Duck",
			"identidad": "Howard (Last name unrevealed)",
			"altura": 79.35,
			"peso": 18.45,
			"fuerza": 2,
			"inteligencia": ""
		}
'''
url_archivo = r"C:\Users\Freelancer\Desktop\pL01_Ejercicios\pL01_PRUEBA_GIT\Clase_PreParcial.py\data_stark (2).json"

def abrir_json(path:str)->list:
	with open(path, "r") as file:
		datos_heroes = json.load(file)
	return datos_heroes["heroes"]

# print(abrir_json())

lista_heroes = abrir_json(url_archivo)

def validar_entero(numero_str: str) -> int:
	result = re.match("^[0-9]+$", numero_str)
	if result != None:
		return int(numero_str)
	else:
		False

def validar_respuesta(a_validar:str, patron_valicion)-> bool or int:

    respuesta_validada = re.search(patron_valicion, a_validar, re.IGNORECASE)
    if( respuesta_validada != None):
        a_validar = a_validar.lower()
        a_validar = a_validar.replace(" ","")
        return a_validar
    else: return False


def listado_heroes(lista_heroes: list):
	'''
	Listar los primeros N héroes.
	El valor de N será ingresado por el usuario  (Validar que no supere max. de lista)

	'''

	cant_heroes = (input("Ingrese la cantidad de heroes a listar: \n"))
	cant_heroes = validar_entero(cant_heroes)
	if cant_heroes != False:
		if cant_heroes > len(lista_heroes):
			print("La cantidad ingresada no es valida, ingrese nuevamente: \n")
		else:
			for i in range(cant_heroes):
				print(lista_heroes[i])
	else:
		print("El caracter ingresado no es valido")

# listado_heroes(lista_heroes)


def buscar_minimo(lista_heroes: list,clave:str) -> int:
	minimo = 0
	for i in range(len(lista_heroes)):
		if lista_heroes[i][clave] < lista_heroes[minimo][clave]:
			minimo = i
	return minimo


def buscar_maximo(lista_heroes:list,clave:str) -> int:
	maximo = 0
	for i in range(len(lista_heroes)):
		if lista_heroes[i][clave] > lista_heroes[maximo][clave]:
			maximo = i
	return maximo


# def lista_minimo(lista_heroes: list) -> list:
# 	lista_original = lista_heroes.copy()
# 	lista_heroes = []

# 	while len(lista_original) > 0:
# 		minimo = buscar_minimo(lista_original)
# 		lista_heroes.append(lista_original.pop(minimo))

# 	return lista_heroes


# def lista_maximo(lista_heroes: list) -> list:
	lista_original = lista_heroes.copy()
	lista_heroes = []

	while len(lista_original) > 0:
		maximo = buscar_minimo(lista_original)
		lista_heroes.append(lista_original.pop(maximo))

	return lista_heroes


def lista_ordenada_altura(lista_heroes: list,orden_lista:str) -> list:
	'''
	Ordenar y Listar héroes por altura.
	Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’)
	'''
	# orden_lista = input("Ingrese com odesea ordenar la lista. \n"
	# 					"asc- para ascendente \n"
	#  					"dsc- para descendente \n\n")
	validar = re.search('asc|desc', orden_lista, re.IGNORECASE)
	orden_lista = orden_lista.lower()

	copia_lista_heroes = lista_heroes.copy()
	lista_heroes_ordenenada = []

	while len(copia_lista_heroes) > 0:
		if orden_lista == "asc":
			minimo = buscar_minimo(copia_lista_heroes, "altura")
			lista_heroes_ordenenada.append(copia_lista_heroes.pop(minimo))
		elif orden_lista == "dsc":
			maximo = buscar_maximo(copia_lista_heroes, "altura")
			lista_heroes_ordenenada.append(copia_lista_heroes.pop(maximo))
		else:
			print("Valor ingresado no valido")
	for heroe in lista_heroes_ordenenada:
		print(heroe["nombre"],heroe["altura"],"cm")
	return lista_heroes_ordenenada

# lista_ordenada_altura(lista_heroes)


def lista_ordenada_fuerza(lista_heroes: list,orden_lista:str) -> list:
	'''
	Ordenar y Listar héroes por fuerza.
	Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’)

	'''
	# orden_lista = input("Ingrese com odesea ordenar la lista. \n"
	# 					"asc- para ascendente \n"
	#  					"dsc- para descendente \n\n")

	copia_lista_heroes = lista_heroes.copy()
	lista_heroes_ordenenada = []

	while len(copia_lista_heroes) > 0:
		if orden_lista == "asc":
			minimo = buscar_minimo(copia_lista_heroes, "fuerza")
			lista_heroes_ordenenada.append(copia_lista_heroes.pop(minimo))
		elif orden_lista == "dsc":
			maximo = buscar_maximo(copia_lista_heroes, "fuerza")
			lista_heroes_ordenenada.append(copia_lista_heroes.pop(maximo))
	for heroe in lista_heroes_ordenenada:
		print(heroe["nombre"],heroe["fuerza"])
	return lista_heroes_ordenenada

# lista_ordenada_fuerza(lista_heroes)

def calcular_promedio_keys(lista_heroes:list, key:str, condicion:str)-> list:
	'''
	Calcular promedio de cualquier key numérica,
	filtrar los que cumplan con la condición de superar o no el promedio
	(preguntar al usuario la condición: ‘menor’ o ‘mayor’)
	se deberá listar en consola aquellos que cumplan con ser mayores o menores según corresponda.
	'''
	cantidad_heroes = len(lista_heroes)
	acumulador_keys = 0
	lista_condicion = []

	for heroe in lista_heroes:
		acumulador_keys += heroe[key]
	promedio_keys = acumulador_keys / cantidad_heroes
	print("El promedio es: {0}".format(promedio_keys))
	for heroe in lista_heroes:
		if condicion == "menor"and heroe[key] < promedio_keys:
				lista_condicion.append(heroe)
		elif condicion == "mayor"and heroe[key] > promedio_keys:
				lista_condicion.append(heroe)
	print(lista_condicion)
	return lista_condicion

#print(calcular_promedio_keys(lista_heroes, "altura","mayor"))

def listado_inteligencia(lista_heroes:list,patron:str)->list:
	'''
	Buscar héroes por inteligencia [good, average, high]
	y listar en consola los que cumplan dicha búsqueda.
	'''
	for heroe in lista_heroes:
		if re.search(patron,heroe["inteligencia"],re.IGNORECASE):
			print("{0} - {1}".format(heroe["nombre"], heroe["inteligencia"]))
	return 

# print(listado_inteligencia(lista_heroes))

# def mostrar(lista_recibida:list, clave="peso"):
# 	file_contenido=""
# 	for heroe in lista_recibida:
# 			file_contenido += "{0},{1},{2}\n".format(heroe["nombre"], heroe["identidad"],heroe[clave])
# 	return file_contenido
# def export_to_csv(file_contenido:list, nombre_archivo:str):

# 	'''
# 	 Exportar a CSV la lista de héroes ordenada según opción elegida anteriormente [1-4]
# 	'''
# 	with open(nombre_archivo,"w+") as file:
# 		for heroe in lista_heroes:
# 			file_contenido = "{0}, {1}\n".format(heroe["nombre"], heroe["identidad"])
# 			file.write(file_contenido)

def mostrar(lista_heroes:list):
    mensaje = ""
   
    for heroe in lista_heroes:
        mensaje += "{0}, {1}, {2}, {3}, {4}, {5}\n".format(heroe["nombre"],heroe["identidad"],heroe["altura"]
        ,heroe["peso"],heroe["fuerza"],heroe["inteligencia"])
    return mensaje
        
def export_to_csv(mensaje:str,nombre_archivo:str):
    '''Exportar a CSV la lista de héroes ordenada según opción elegida anteriormente [1-4]'''
    
    nombre_archivo = "data_stark.csv"
    with open(nombre_archivo, "w+") as archivo:
        archivo.write(mensaje)



	