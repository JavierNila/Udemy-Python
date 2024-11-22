mi_lista = ['a','b','c']
resultado = len(mi_lista)
print(type(mi_lista))
print(resultado)

resultado = mi_lista[0:]
print(resultado)

mi_lista2 = ['d','e','f']
print(mi_lista + mi_lista2)
print(mi_lista)
print(mi_lista2)

mi_lista3 = mi_lista + mi_lista2

#mi_lista3[0] = 'alfa'
#mi_lista3.append('g')
eliminado = mi_lista3.pop(0)

print(mi_lista3)
print(eliminado)
print("---------------------------------")

lista = ['g','o','b','m','c']
nueva_lista = lista.sort()
print(type(nueva_lista))

lista.sort()
lista2 = lista
print(lista2)

lista.reverse()
print(lista)
