mi_archivo = open('Prueba.txt')

'''una_linea = mi_archivo.readline()
print(una_linea)

una_linea = mi_archivo.readline()
print(una_linea)

una_linea = mi_archivo.readline()
print(una_linea)'''

#Se vuelve una lista con el readlines
todas = mi_archivo.readlines()

todas = todas.pop()

print(todas)

mi_archivo.close()