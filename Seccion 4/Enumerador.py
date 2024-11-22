lista = ['a','b','c']

for item in enumerate(lista):
    print(item)

print("\n")

lista = ['a','b','c']

for indice,item in enumerate(range(50,55)):
    print(indice,item)

print("\n")

lista = ['a','b','c']

mis_tuples = list(enumerate(lista))
print(mis_tuples)