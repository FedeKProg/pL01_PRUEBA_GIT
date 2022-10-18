lista_precios = {

	"banana" : {
		"precio" : 120.10,
		"unidad_medida": "kg",
		"stock": 50
	},

	"pera": {
		"precio": 240.50,
		"unidad_medida": "kg",
		"stock": 40
	},

	"frutilla": {
		"precio": 300,
		"unidad_medida": "kg",
		"stock": 100
	},

	"mango" : {
		"precio": 300,
		"unidad_medida": "unidad",
		"stock": 100
	}

}

import re

# Punto 1: solicitar al usuario un producto y verificiar si existe en 'lista_precios' en caso de existir mostrar precio y el stock. En caso de no existir el
# producto mostrar el mensaje 'el articulo no se encuentra en la lista'

def busqueda_productos(lista_precios:dict,patron:str):
	'''
	Buscar si los productos estan dentro de la lista
	y listar en consola los que cumplan dicha búsqueda.
	'''

	patron = input("Ingrese el produto a buscar\n\n")

	busqueda_producto = lista_precios.get(patron, None)

	if busqueda_producto == None:
		print("el articulo no se encuentra en la lista")
	else:
		print("Producto: {0} \nPrecio: {1} \nstock {2}".format(patron, busqueda_producto["precio"], busqueda_producto["stock"]))

# print(busqueda_productos(lista_precios, "banana"))

# Punto 2: agregar al punto anterior que el usuario ingrese la cantidad y retornar el precio total (precio * cantidad)

def busqueda_precio(lista_precios:dict,patron:str):
	'''
	Buscar si los productos estan dentro de la lista
	y listar en consola los que cumplan dicha búsqueda.
	'''

	patron = input("Ingrese el produto a buscar\n")
	cantidad = input("Ingrese la cantidad a comprar del producto \n\n")

	busqueda_producto = lista_precios.get(patron, None)

	if busqueda_producto == None:
		print("el articulo no se encuentra en la lista")
	else:
		cantidad = float(cantidad)
		print("Producto: {0} \nPrecio: {1} \nstock {2}".format(patron, busqueda_producto["precio"], busqueda_producto["stock"]))
		precio = float(busqueda_producto["precio"])
		precio_final = cantidad * precio
		print("El precio total es {0}".format(precio_final))



# Punto 3: solicitar al usuario que ingrese una nueva fruta junto con su precio, unidad de medida y stock. Agregar la nueva fruta a la lista de precios

def agregar_fruta(lista_precios: dict, elemento:str):
	nueva_fruta = input("Ingrese una fruta nueva\n")
	precio_nuevo = float(input("Ingrese el precio de la fruta\n"))
	u_medidad_nueva = input("Ingrese la unidad de medida del producto(unidad o por kg)\n")
	stock_nuevo = int(input("Ingrese la cantidad del producto disponible en stock\n"))

	lista_precios.update({nueva_fruta:{"precio": precio_nuevo, "unidad_medida": u_medidad_nueva, "stock": stock_nuevo}})

	print(lista_precios)

# print(agregar_fruta(lista_precios,"manzana"))
# Punto 4: imprimir el listado de frutas (solo su nombre)

def imprimir_nombre_fruta():

	for fruta in list(lista_precios.keys()):
		print("Nombre fruta: {0}".format(fruta))

lista_nombres = imprimir_nombre_fruta
print(lista_nombres)

# Punto 5: solicitarle al usuario el nombre de fruta y en caso de exisitir eliminarla. En caso de que el producto no exista mostrar
# el mensaje 'el articulo no se encuentra en la lista'

def eliminar_productos(lista_precios:dict,patron:str):
	'''
	Buscar si los productos estan dentro de la lista
	y listar en consola los que cumplan dicha búsqueda.
	'''

	patron = input("Ingrese el produto a eliminar\n\n")

	busqueda_producto = lista_precios.get(patron, None)

	if busqueda_producto == None:
		print("el articulo no se encuentra en la lista")
	else:
		lista_precios.pop(patron)
		print(lista_precios)

# print(eliminar_productos(lista_precios,"banana"))