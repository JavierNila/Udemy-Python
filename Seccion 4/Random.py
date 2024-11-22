from random import *

aleatorio1 = randint(1,50)
print(aleatorio1)

print("\n")

aleatorio2 = uniform(1,5)
print(aleatorio2)

print("\n")

aleatorio3 = random()
print(aleatorio3)

print("\n")

colores = ['rojo','azul','verde','amarillo']
aleatorio4 = choice(colores)
print(aleatorio4)

print("\n")

numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)
