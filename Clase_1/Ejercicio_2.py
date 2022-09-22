

total_Kilos = 0
acumulador_Kilos = 0
acumulador_Precio = 0
Descuento_Cien_Kilos = 0.85
Descuento_Trescientos_Kilos = 0.75
continuar = True
producto_Caro = 0
flag = 0
mensaje = ""


while True:
		peso=int(input("Ingrese el peso del alimento ( entro 10 y 100 kilos): "))
		while(peso<10 and peso>100):
			peso = int(input("El peso ingresado no es valido"))	

		precio_Kilo=int(input("Ingrese el precio por kilo del producto: "))
		while(precio_Kilo<250):
			precio_Kilo=int(input("El valor ingresado no esta dentro de los aceptados."))	

		tipo_producto = (input("Ingrese el tipo de prodcucto( v para vegetal, a para animal y m para mezcla: "))
		while(tipo_producto != "v" and tipo_producto != "a" and tipo_producto != "m"):
			tipo_producto = (input("El tipo de producto es invalido. Ingrese nuevamente."))

		acumulador_Kilos+=peso
		acumulador_Precio+=precio_Kilo
		precio_Final = acumulador_Kilos * acumulador_Precio

		if(acumulador_Kilos > 100 and acumulador_Kilos < 300):
			precio_Descuento = precio_Final * Descuento_Cien_Kilos
			mensaje_Desc = "El importe con descuento es de: " + str(precio_Descuento)
		
		elif(acumulador_Kilos < 300):
			precio_Descuento = precio_Final * Descuento_Trescientos_Kilos
			mensaje_Desc = "El importe con descuento es de: " + str(precio_Descuento)
		else:
			precio_Descuento = precio_Final
			mensaje_Desc = "El importe con descuento es de: " + str(precio_Descuento)

		if (flag == 0 or producto_Caro > precio_Kilo):
			producto_Caro = precio_Kilo
			tipo_Producto_Caro = tipo_producto

		respuesta = input("Quiere sumar otro producto? (si o no)")
		if respuesta == "no":
			break

promedio = acumulador_Precio / acumulador_Kilos

mensaje = input("\nEl importe total a pagar sin descuento es: " + str(precio_Final) + "\n" + mensaje_Desc
		+ "\n" + "El tipo de alimento mas caro es: " + str(tipo_Producto_Caro)
		+ "\n" + "El promedio de precio por kilo final es: " + str(promedio) + "\n")




