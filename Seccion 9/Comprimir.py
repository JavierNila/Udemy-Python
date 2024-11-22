import zipfile
import shutil

# Este es para comprimir
'''mi_zip = zipfile.ZipFile('archivo_comprimido.zip', 'w')

mi_zip.write('mi_texto_A.txt')
mi_zip.write('mi_texto_B.txt')

mi_zip.close()'''


# Este es para descomprimir
'''zip_abierto = zipfile.ZipFile('archivo_comprimido.zip', 'r')

zip_abierto.extractall()'''


# Comprimir un archivo pero usando shutil
'''carpeta_origen = 'C:\\Users\\SPARTAN PC\\Desktop\\Carpeta_Superior'

archivo_destino = 'Todo_Comprimido'

shutil.make_archive(archivo_destino, 'zip', carpeta_origen)'''


# Descomprimir un archivo con shutil
'''shutil.unpack_archive('Todo_Comprimido.zip', 'Extraccion Terminada', 'zip')'''
