nombre = input("Cual es tu nombre? ")
ventas = float(input("Cuanto vendiste? "))
comisiones = round(ventas * 13/100,2)

print(f"Hola {nombre} en este mes vendiste ${ventas}, considerando eso el monto de comisiones que te corresponde es de ${comisiones}")


#Esta es la forma del instructor
nombre = input("Por favor, dime tu nombre: ")
ventas = input("Diga sus ventas totales del mes: ")

ventas = int(ventas)

comision = ventas * 13/100

comision = round(comision,2)

print(f"Hola {nombre}, tus comisiones de este mes son {comision}")

#Mi codigo esta bien puede ser tanto integer (int) o float :D
#La legibilidad, ambos estan bien, el del instructor muestra los pasos uno por uno y el mio acorta esos pasos en menos lineas