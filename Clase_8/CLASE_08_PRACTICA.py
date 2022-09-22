

def parse_json(data_stark:str)->list:
    dic_json = {}
    with open(data_stark, "r") as archivo:
        dic_json = json.load(archivo)
    return dic_json["heroes"]

lista_heroes = parse_json("C:\Users\Freelancer\Desktop\pL01_Ejercicios\pL01_PRUEBA_GIT\Clase_8\data_stark.json")
print(lista_heroes)