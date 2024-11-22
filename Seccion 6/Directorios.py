import os
from pathlib import Path

#ruta de mi archivo
'''ruta = os.getcwd()'''

#Para cambiar de directorio
#Para poner otra ruta es usar la barra invertida dos veces para que la tome en cuenta
'''ruta = os.chdir('C:\\Users\\Win10\\Desktop\\Alternativo')'''

#Para crear directorios
'''ruta = os.mkdir('C:\\Users\\Win10\\Desktop\\Alternativo\\otra')'''

'''ruta = 'C:\\Users\\SPARTAN PC\\Documents\\PYTHON\\Seccion 6\\Prueba.txt'''
#Para la base de la ruta
'''elemento = os.path.basename(ruta)'''
#Para el directorio de la ruta
'''elemento = os.path.dirname(ruta)'''

#Separado por una tupla
'''elemento = os.path.split(ruta)'''

#Para eliminar directorio se pone al final la carpeta que se quiere eliminar, en este caso "otra"
'''os.rmdir('C:\\Users\\Win10\\Desktop\\Alternativo\\otra')'''

#Se pueden abrir archivos en otros directorios de esta forma tambien
'''otro_archivo = open('C:\\Users\\Win10\\Desktop\\Alternativo\\otro_archivo.txt')'''

#Una forma de leer los archivos con el formato de otro sistema operativo como lo es MAC usando PATH
'''carpeta  = Path('C:/Users/Win10/Desktop/Alternativo')
archivo = carpeta / 'otro_archivo.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())'''