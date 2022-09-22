
edad_Heroe_Joven = 0
nombre_Heroe_Joven = 0
edad_Heroe_Mayor = 0
sexo_Heroe_Mayor = 0
nombre_Heroe_Mayor = 0
flag = 0
contador_Heroinas = 0
contador_Heroinas_Fuerza = 0
contador_Fuerza = 0
contador_Edad = 0
contador_Edad_Heroinas = 0


while(True):

    nombre=input("Ingrese el nombre del heroe/heroina: ")
    while (nombre == ""):
        nombre = input("El nombre ingresado no es valido ")

    edad=int(input("Ingrese ela edad del heroe o heroina: "))
    while(edad<18):
        edad=int(input("la edad ingresada no esta dentro de los aceptados. "))	

    sexo = (input("Ingrese el sexo se su heroe o heroina(f, m o nb): "))
    while(sexo != "m" and sexo != "f" and sexo != "nb"):
        sexo = (input("El sexo es invalido. Ingrese nuevamente. "))

    habilidad = (input("Ingrese el tipo de habilidad (fuerza, magia o inteligencia): "))
    while(habilidad != "fuerza" and habilidad != "magia" and habilidad != "inteligencia"):
        habilidad = (input("La habilidad es invalida. Ingrese nuevamente. "))

    if(sexo == "f"):
        contador_Heroinas +=1
        contador_Edad_Heroinas += edad

    if(flag == 0 or edad_Heroe_Joven < edad):
        if (habilidad == "fuerza"):
            flag = 1
            edad_Heroe_Joven = edad
            nombre_Heroe_Joven = nombre

    if (flag == 0 or edad_Heroe_Mayor < edad):
        flag = 1
        edad_Heroe_Mayor = edad
        sexo_Heroe_Mayor = sexo
        nombre_Heroe_Mayor = nombre

    if (flag == 0 or sexo == "f"):
        if (habilidad == "fuerza" or habilidad == "magia"):
            contador_Heroinas_Fuerza +=1

    if(habilidad == "fuerza"):
        contador_Fuerza +=1
    
    contador_Edad += edad

    respuesta = input("Quiere sumar otro heroe/heroina? (si o no)")
    if respuesta == "no":
        break

promedio_Edad_Fuerza = contador_Edad * contador_Fuerza
promedio_Edad_Heroinas = contador_Edad_Heroinas / contador_Heroinas

mensaje = input("El nombre del heroe/heroina de fuerza con menor edad es: " + str(nombre_Heroe_Joven) + "\n" 
    + "El nombre del heroe/heroina con mayor edad es: " + str(nombre_Heroe_Mayor) + " Y es de sexo: " + str(sexo_Heroe_Mayor) + "\n"
    + "La cantidad de heroinas que tienen habialidad de fuerza o magia son: " + str(contador_Heroinas_Fuerza) + "\n"
    + "El promedio de edad entre heroinas es de: " + str(promedio_Edad_Heroinas))

 