'''def mi_funcion():
    lista = []
    for x in range(1,5):
        lista.append(x * 10)
    return lista


def mi_generador():
    for x in range(1,5):
        yield x * 10


print(mi_funcion())
print(mi_generador())

g = mi_generador()

print(next(g))
print(next(g))
print(next(g))
print(next(g))'''


def mi_generador():
    x = 1
    yield x

    x += 1
    yield x

    print("Hola mundo")

    x += 1
    yield x


g = mi_generador()

print(next(g))
print(next(g))
print(next(g))

print("\n")


def mi_generador():
    numero = 1
    while True:
        yield numero
        numero += 1


generador = mi_generador()
print(next(generador))

print("\n")


def mi_generador():
    numero = 7
    while True:
        yield numero
        numero += 7


generador = mi_generador()
print(next(generador))

print("\n")


def vidas_personaje():
    vidas = 3
    while vidas > 0:
        if vidas == 1:
            yield f'Te queda {vidas} vida'
        else:
            yield f'Te quedan {vidas} vidas'
        vidas -= 1
    yield 'Game Over'


perder_vida = vidas_personaje()


