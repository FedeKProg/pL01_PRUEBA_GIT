
'''
Python oriendato a objetos
desarrolo de distinto metodos a implementar en el codigo

POO es un metodo para estructurar el codigo mediante la agrupacion de 
propiedades y comporatmientos relacionados en objetos individuales

Objeto = persona x ej, pero puede ser un auto, una piedra un bloque, etc
Propiedades/atributos = nombre, edad, etc
Comportamiento/metodo = Correr, caminar, etc

'''
#listas

#diccionario

#clases

class Personaje:

	#tipo = "Personaje" #definir atributos de clase

	#Definir las propiedades/atributos del objeto/clase
	def __init__(self,id,Nombre,apellido,edad) -> None:

		super().__init__()
		self.id = id
		#atributo protegido (no se puede modificar por fuera de la funcion) un solo guion bajo
		self._nombre = Nombre
		#Atributo privado (no se puede modificar por fuera de la funcion) doble guion bajo
		self.__apellido = apellido
		self.edad = edad

		#definir metodos
		def mostrar(self):
			print(self._nombre)


		#la funcion del getter y setter debe llamarse igual
		@property
		def nombres(self): #Getter
			return self._nombre
		@nombres.setter #Nombre de la funcion + setter
		def nombres(self,nombre): #Setter
			self._nombre = nombre

		def __str__(str): #devuelve la variablke como string
			return self._nombre + "HOLA"

		def __len__(self):#devuevle la variable como entero
			return 14

		def __getitem__(self,index):
			if index == "nombre":
				return self._nombre
			else:
				return ""

		def __setitem__(self,index,valor):
			if index == "nombre":
				return self._nombre == valor

		def __iter__(self):
			for i in self.lista:
				yield i 
'''
	Metodo Dunder o Magico = son los metodos de una clase de doble subrayado
'''


aux_personaje = Personaje(5, "Fede", "Katri", 22)
print(aux_personaje)





