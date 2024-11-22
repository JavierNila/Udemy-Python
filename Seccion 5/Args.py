def suma(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(suma(5,6,9,10,500))

print("\n")

def suma_cuadrados(*args):
    suma = 0
    for arg in args:
        suma += arg ** 2
    return suma

print(suma_cuadrados(1,2,3))

print("\n")

def suma_absolutos(*args):
    suma = sum(abs(arg) for arg in args )
    return suma

print(suma_absolutos(1,2,54,-8))

print("\n")

def numeros_persona(nombre,*args):
    suma_numeros = sum(abs(arg)for arg in args)
    return (f"{nombre}, la suma de tus números es {suma_numeros}")

print(numeros_persona('pedro',40,50,90))