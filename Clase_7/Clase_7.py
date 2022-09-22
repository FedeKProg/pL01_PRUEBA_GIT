import re
texto = "uno 1 dos 2 tres 3 cuatro 4"
lista = re.split('[0-9]+', texto)
print(re.split('[0-9]+', texto))
print(re.split('[a-z ]+', texto))
print (lista[0])