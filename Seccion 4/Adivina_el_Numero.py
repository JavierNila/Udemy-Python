from random import *

#Mi forma de hacerlo
nombre = input("¿Cual es tu nombre? ")
print(f"Encantado {nombre}, he pensado en un numero entre 1 y 100, tienes 8 intentos para adivinar.")

numero = randint(1,101)
intentos = 8

for i in range(1,intentos + 1):
    respuesta = int(input("Que numero eliges? "))
    if respuesta not in range(1,101):
        print("No se encuentra en el rango ese numero, elige otro")
    elif respuesta > numero:
        print("Has elegido un numero mayor al correcto, elige otro")
    elif respuesta < numero:
        print("Has elegido un numero menor al correcto, elige otro")
    elif respuesta == numero:
        print("Adivinaste, muchas felicidades!")
        print(f"Lo conseguiste en el intento numero {i}")
        break
else:
    print(f"Te quedaste sin intentos, la respuesta era {numero}")

print("\n")

#Forma del instructor
'''intentos = 0
estimado = 0
numero_secreto = randint(1,100)
nombre = input("Dime tu nombre: ")

print(f"Bueno {nombre}, he pensado en un número entre 1 y 100\nTienes 8 intentos para adivinar")

while intentos < 8:
    estimado = int(input("Cual es el numero?: "))
    intentos += 1

    if estimado not in range(1,101):
        print("Tu numero no se encuentra en el rango que va desde 1 a 100")

    elif estimado < numero_secreto:
        print("Mi numero es mas alto")

    #if estimado > numero_secreto:
    elif estimado > numero_secreto:
        print("Mi numero es mas bajo")

    #if estimado == numero_secreto:
    else:
        print(f"Felicitaciones {nombre}! Has adivinado en {intentos} intentos")
        break

if estimado != numero_secreto:
    print(f"Lo siento, se han agotado los intentos. El numero secreto era {numero_secreto}")'''
