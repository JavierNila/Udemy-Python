palabra = 'python'

lista = [letra for letra in palabra]

print(lista)

print("\n")

lista = [n for n in range(0,21,2)]

print(lista)

print("\n")

lista = [n / 2 for n in range(0,21,2)]

print(lista)

print("\n")

lista = [n for n in range(0,21,2) if n * 2 > 10]

print(lista)

print("\n")

lista = [n if n * 2 > 10 else 'no' for n in range(0,21,2)]

print(lista)

print("\n")

pies = [10,20,30,40,50]
metros = [p / 3.281 for p in pies]

print(metros)