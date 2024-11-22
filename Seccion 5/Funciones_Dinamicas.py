def chequear_3_cifras(lista):

    lista_3_cifras = []

    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass

    return lista_3_cifras

resultado = chequear_3_cifras([555,99,66])
print(resultado)

print("\n")

def todos_positivos(numero):
    for n in numero:
        if n > 0:
            pass
        else:
            return False
    return True

lista_numeros = [12,4,7,6,-3]
print(todos_positivos(lista_numeros))

print("\n")

def suma_menores(numeros):
    suma = 0
    for n in numeros:
        if n in range(0, 1000):
            suma = suma + n
        else:
            pass
    return suma

lista_numeros = [100, 90, 70]
print(suma_menores(lista_numeros))

print("\n")


def cantidad_pares(pares):
    numeros = 0
    for n in pares:
        if n % 2 == 0:
            numeros += 1
    return numeros

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(cantidad_pares(lista_numeros))
