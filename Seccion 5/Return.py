def multiplicar(numero1,numero2):
    total = numero1 * numero2
    return total

resultado = multiplicar(5,200)
print(resultado)

print("\n")

def potencia(num1,num2):
    return num1 ** num2

valores = potencia(3,4)
print(valores)

print("\n")


def usd_a_eur(moneda):
    return moneda * 0.90


dolares = usd_a_eur(1)
print(dolares)

print("\n")

def invertir_palabra(palabra):
    palabra = palabra[::-1]
    palabra = palabra.upper()
    return palabra

palabra = invertir_palabra("Python")
print(palabra)


