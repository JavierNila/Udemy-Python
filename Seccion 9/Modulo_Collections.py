from collections import Counter, defaultdict, namedtuple, deque

numeros = [8, 6, 9, 4, 6, 8, 8, 2, 5, 7, 8, 3, 3]
print(Counter(numeros))
print(Counter('misissipí'))

frase = 'al pan pan y al vino vino'
print(Counter(frase.split()))

serie = Counter([1,1,1,1,1,1,2,2,2,2,3,3,3,3,3,3,3,3,2,2,1,1,4])
print(serie.most_common())
print(list(serie))

'''mi_dic = {'uno': 'verde', 'dos': 'azul', 'tres': 'rojo'}
print(mi_dic['dos'])'''

mi_dic = defaultdict(lambda: 'nada')
mi_dic['uno'] = 'verde'
print(mi_dic['dos'])
print(mi_dic)

'''mi_tupla = (500, 18, 65)
print(mi_tupla[1])'''

Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
ariel = Persona('Ariel', 1.76, 79)
print(ariel.altura)
print(ariel.nombre)
print(ariel.peso)
print(ariel[2])

print("\n")

from collections import Counter

lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]

contador = Counter(lista)

print("\n")

from collections import defaultdict

mi_diccionario = defaultdict(lambda: 'Valor no hallado')
mi_diccionario['edad'] = 44

print("\n")

from collections import deque

ciudades = ["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]

lista_ciudades = deque(ciudades)
print(lista_ciudades)
lista_ciudades.appendleft('Mexico')
print(lista_ciudades)

