def numeros_perfumeria():
    for n in range(1,10000):
        yield f"P - {n:02}"


def numeros_farmacia():
    for n in range(1,10000):
        yield f"F - {n:02}"


def numeros_cosmetica():
    for n in range(1,10000):
        yield f"C - {n:02}"


p = numeros_perfumeria()
f = numeros_farmacia()
c = numeros_cosmetica()


def decorador(rubro):

    print("\n" + "*" * 23)
    print("Su numero es: ")
    if rubro == 'P':
        print(next(p))
    elif rubro == 'F':
        print(next(f))
    else:
        print(next(c))
    print("Aguarde y sera atendido")
    print("*" * 23 + "\n")
