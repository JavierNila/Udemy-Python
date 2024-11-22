monedas = 5

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else:
    print("No tengo mas dinero")

print("\n")

respuesta = 's'

while respuesta == 's':
   respuesta = input("Quieres seguir? (s/n)")
else:
    print("Gracias")

print("\n")
#La palabra pass es para reservar ese espacio y poder pasar al siguiente
# respuesta = 's'
#
# while respuesta == 's':
#     pass
#
# print("Hola")
#
# print("\n")
#La palabra break interrumpe un ingreso de usuario a partir de la iteracion y continue para continuar a partir de la iteracion actual
nombre = input("Tu nombre: ")

for letra in nombre:
    if letra == 'r':
        #break
        continue
    print(letra)

print("\n")

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for numeros in lista_numeros:
    if numeros == -1:
        break
    print(numeros)

