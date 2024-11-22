import random


# Método de burbuja
def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]


# Crear una lista de números aleatorios
n = 10
lista = [random.randint(1, 10) for _ in range(n)]

# Dividir la lista en dos
lista1 = []
lista2 = []
for valor in lista:
    if valor < (n // 2):
        lista1.append(valor)
    else:
        lista2.append(valor)

# Ordenar ambas listas con el método de burbuja
burbuja(lista1)
burbuja(lista2)

# Combinar las dos listas
lista = lista1 + lista2
print(lista1)
print(lista2)
print(lista)