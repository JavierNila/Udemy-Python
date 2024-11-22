archivo = open('Prueba.txt','a')
'''lista = ['Hola','mundo','aqui','estoy']
for p in lista:
    archivo.writelines(p + '\n')'''
archivo.write('bienvenido')

archivo.close()

print("\n")

archivo = open('mi_archivo.txt','w')
cambio = archivo.write('Nuevo texto')
archivo.close()
archivo = open('mi_archivo.txt','r')
leer = archivo.readline()
print(leer)

print("\n")

archivo = open('mi_archivo.txt','a')
cambio = archivo.write("Nuevo inicio de sesión")
archivo.close()
archivo = open('mi_archivo.txt','r')
leer = archivo.read()
print(leer)

print("\n")

archivo = open('registro.txt', 'a')

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

for p in registro_ultima_sesion:
    archivo.writelines(p + '\t')

archivo.close()

archivo = open('registro.txt', 'r')
leer = archivo.read()
print(leer)