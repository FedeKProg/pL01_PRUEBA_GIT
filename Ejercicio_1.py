
#from ctypes.wintypes import INT


#from enum import Flag

var = 0
flag=0
barbijo_Caro = 0
unidad_Barbijo_Caro = 0
fabircant_Barbijo_Caro = ""
item_Mas_Unidades = 0
item_Mas_Unidades_Fabricante = "" 
contador_Jabon = 0
cant_Jabon = 0

for i in range(5):
		
	tipo_Producto = input("Ingrese un producto de prevencíon de contagios. Puede ser: alcohol, barbijo o jabon: ")
	while(tipo_Producto != "barbijo" and tipo_Producto != "jabon" and tipo_Producto != "alcohol"):
		tipo_Producto = input("El producto ingresado no es valido")
		
	precio = int(input("Ingrese el precio del producto (entre 100 y 300)."))
	while(precio < 100 or precio > 300):
		precio = int(input("El valor ingresado no esta dentro de los aceptados."))
		
	cant_Productos = int(input("Ingrese la cantidad de unidades del producto (entre 0 y 1000)"))
	while(cant_Productos < 0 or cant_Productos > 1000):
		cant_Productos = int(input("Cantidad de unidades invalida. Ingrese nuevamente."))		

	marca = input("Ingrese la marca del producto.")
	fabricante = input("Ingrese el fabricante del producto.")

if flag == 0 or barbijo_Caro < 0:
            barbijo_Caro = precio
            unidad_Barbijo_Caro = cant_Productos
            fabircant_Barbijo_Caro = fabricante

if flag == 0 or item_Mas_Unidades < cant_Productos:
            item_Mas_Unidades = cant_Productos
            item_Mas_Unidades_Fabricante = fabricante
        
if tipo_Producto == "jabon":
            contador_Jabon += 1
            cant_Jabon = cant_Productos * contador_Jabon

print("El mas caro de los barbijos tiene una cantidad de: " + str(unidad_Barbijo_Caro) + " unidades y es fabricado por: " + str(fabircant_Barbijo_Caro) +  
    "\n El item con mas unidades es fabricado por: " + str(item_Mas_Unidades_Fabricante) + 
    "\n La cantidad de jabones es: " + str(cant_Jabon) + 
    "\n Gracias por usar el programa!")

		# 		#if(precio < alcoholBarato || banderaAlcoholBarato == false):
		# 			banderaAlcoholBarato = true;
		# 			alcoholBarato = precio;
		# 			cantAlcoholBarato = cant_Productos;
		# 			fabAlcoholBarato = fabricante;
        #             acumulador_Alcohol += cant_Productos
				
		# 	break;
		# 	case "barbijo":
		# 		acumuladorBarbijo += cantProductos;
		# 		contadorBarbijo++
		# 	break;
		# 	default:
		# 		acumuladorJabon += cantProductos;
		# 		contadorJabon++;
		

		# 	listaProductos = "Tipo de producto: " + tipoProducto + "<br>" +
		# 	"Precio del producto: " + precio + "<br>" +
		# 	"La cantidad de unidades son: " + cantProductos + "<br>" +
		# 	"La marca es: " + marca + "<br>" +
		# 	"Y el fabricante es: " + fabricante + "<br>---------------------------------------------------<br>"; 
		# 	document.write(listaProductos);
	
		# masUnidades = Math.max(acumuladorAlcohol, acumuladorBarbijo, acumuladorJabon);

		# switch(masUnidades)
		# 	case"alcohol": 
		# 		mensaje = "El tipo de producto con mas unidades compradas es el Alcohol, con un promedio de "; 
		# 	break:
		# 	case "barbijo":
		# 		mesaje = "El tipo de producto con mas unidades compradas es el Barbijo, con un promedio de "; 
		# 	break:
		# 	default:
		# 		mensaje = "El tipo de producto con mas unidades compradas es el Jabon, con un promedio de "; 
		

		# switch(promedioMasUnidades)
		# 	case"alcohol":
		# 		promedioMasUnidades = acumuladorAlcohol / cantProductos;
		# 		mensajePromedio = "El alcohol fue el que mas unidades se eligio con un promedio de: ";
		# 	break;
		# 	case "barbijo":
		# 		promedioMasUnidades = acumuladorBarbijo / cantProductos;
		# 		mensajePromedio = "El barbijo fue el que mas unidades se eligio con un promedio de: ";
		# 	break;
		# 	default:
		# 		promedioMasUnidades = acumuladorJabon / cantProductos;
		# 		mensajePromedio = "El jabon fue el que mas unidades se eligio con un promedio de: ";
		

		# cantJabon = acumuladorJabon;
		# mensjaeJabon = "La cantidad de jabones comprados es: " + cantJabon;

		# listaFinal = "El mas barato de los alcoholes tiene un precio de: " + alcoholBarato +
		# " Y se compro un total de " + cantAlcoholBarato + " unidades. Y fue fabricado por: " + fabAlcoholBarato + "<br>" +
		# " El tipo de producto con mas unidades vendidas es: " + masUnidades + " Con un promedio por compra de: " + promedioMasUnidades + "<br>" +
		# "Hay un total de: " + cantJabon + " unidades de jabon";
		# document.write(listaFinal); 