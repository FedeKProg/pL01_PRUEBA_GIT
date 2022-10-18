# MIT License
#
# Copyright (c) 2022 [UTN FRA](https://fra.utn.edu.ar/) All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from random import randint


lista_palabras = [
	"Goku", "Vegeta", "Frieza", "Cell", "Beerus", 'Krillin'
]

# Refactoprizar la funcion clasica usando lambda
def sup_triangulo(base: int, altura: int) -> float:
	return (base*altura)/2

superficie_triangulo = lambda b, a, c : (b*a)/c
print("La superficie es: {0}".format(superficie_triangulo (5,9,2)))


# Refactorizar la funcion clasica usando lambda y map
def aplicar_mayusculas(lista_palabras: list) -> list:
	for i in range(len(lista_palabras)):
		lista_palabras[i] = lista_palabras[i].upper()
	return lista_palabras
lista_mayuscula = list(map(str.upper,lista_palabras))
print(lista_mayuscula)

'''
# Refactorizar la funcion usando lambda y reduce
def obtener_mas_letras(lista: list) -> str:
	seleccionado = ''
	for palabra in lista:
		if len(palabra) > len(seleccionado):
			seleccionado = palabra
	return seleccionado
'''
from functools import reduce

# def comparar_palabras (palabra_1:str, palabra_2:str)->str:
# 	if len(palabra_1) > len(palabra_2):
# 		return palabra_1
# 	else:
# 		return palabra_2
comparar_palabras = lambda palabra_1, palabra_2: palabra_1 if len(palabra_1) > len(palabra_2) else palabra_2

palabra_larga = reduce(comparar_palabras, lista_palabras)
print(palabra_larga)


# refactorizar la funcion usando lambda y filter
def obtener_nombres_cantidad_letras(lista: list, cantidad: int) -> list:

	cant_letras = lambda elem: len(elem) == cantidad
	lista_cantidad = list(filter(cant_letras,lista))
	print(lista_cantidad)
	return lista_cantidad
print("La lista ordenada segun la cantidad de letras es: {0}".format(obtener_nombres_cantidad_letras(lista_palabras,6)))

	# seleccionados = list()
	# for palabra in lista:
	# 	if len(palabra) == cantidad:
	# 		seleccionados.insert(0, palabra)
	# return seleccionados

# refactorizar usando shuffle
def ordenar_random_lista(lista: list) -> list:
	maximo = len(lista)
	desordenada = list()
	while len(desordenada) < len(lista):
		indice = randint(0, maximo)
		for elemento in lista:
			desordenada.insert(indice, elemento)
	return desordenada

# Refactorizar usando sort y lamda
def ordenar_burbujeo(lista: list) -> list:
	lista_copia = lista.copy()
	for i in range(len(lista_copia)-1):
		for j in range(i+1, len(lista_copia)):
			if lista_copia[i] > lista_copia[j]:
				lista_copia[i], lista_copia[j] = lista_copia[j], lista_copia[i]
	return lista_copia


heroes = [
	"goKU", "vEgETa", 'kriLLin'
]

villanos = [
	"FrIEzA", "CELl", "Majin Buu"
]

ataques = [
	"Kame hame ha", "Final flash", "Kienzan"
]

# Refactorizar usando zip
for ind_h in range(len(heroes)):
	for ind_a in range(ind_h, len(ataques)):
		for ind_v in range(ind_h, len(villanos)):
			mensaje =\
				f"""
				{heroes[ind_h].capitalize()}
				Lanza un {ataques[ind_a].capitalize()}
				a {villanos[ind_v].capitalize()}
				"""
			print(mensaje)
			break
		break
