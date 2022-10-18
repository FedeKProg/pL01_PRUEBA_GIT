from dataclasses import replace


persona_1 = {
    "nombre": "Maximo",
    "apellido": "Cozzetti",
    "domicilio": {
        "calle": "Av. Mitre",
        "altura": 750,
        "localidad": "Avellaneda",
        "barrio": "Avellaneda Centro",
        "cod_postal" : "C1870"
    },    
    "telefonos": [
        {
            "etiqueta": "fijo",
            "cod_pais": "+54",
            "cod_area": "11",
            "numero": "4201-4133"
        },
        {
            "etiqueta": "movil",
            "cod_pais": "+54",
            "cod_area": "11",
            "nro": "4353-0220"
        }
    ],
    
    "identificacion": {
        "tipo": "dni",
        "nro": "30.505.003"
    }
}


# Punto 1: Modificar la calle y altura de 'persona_1' por Ramón Franco 5050. 



# Punto 2: Verificar si existe un numero de telefono con la etiqueta 'trabajo'. Si no existe, entonces crearlo con el valor +54 11 4201-4133. Caso contrario actualizarlo


# Punto 3: imprimir los datos completos de persona_1 recorriendo todas sus claves y valores


# Punto 4: 
#   Obtener el id de 'persona_1' y de 'persona_2'. 
#   Comprarlos, si son iguales imprirmir: 
#       "'ID de persona_1 es: id_persona_1 y el ID de persona_2 es: id_persona_2 entonces son el mismo diccionario' caso contrario imprimir "No son el mismo diccionario"
#   Modificar el nombre y apellido de persona_1 por Emilio Ravenna
#   Imprimir persona_1 y persona_2 y analizar los resultados
persona_2 = persona_1



# Punto 5: 
#   Crear persona_3 a partir de una copia superficial de persona_1
#   Modificar nombre y apellido a persona_3 por Gabriel Medina
#   Modificar el nro de documento por 28.307.401
#   Imprimir persana_1 y persona_3 y analizar los resultados



# Punto 6: 
#   Crear persona_4 a partir de una copia profunda de persona_1
#   Modificar el nombre y apellido por Mario Santos
#   Modificar el nro de documento por: 29.407.901
#   Imprimir persana_1 y persona_3 y analizar los resultados