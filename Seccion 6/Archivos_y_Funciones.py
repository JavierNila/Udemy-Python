def abrir_leer(archivo):
    abrir = open(archivo)
    return abrir.read()

print("\n")

def sobrescribir(archivo):
    abrir = open(archivo, 'w')
    cambiar = abrir.write("contenido eliminado")

print("\n")

def registro_error(archivo):
    abrir = open(archivo, 'a')
    cambio = abrir.write("se ha registrado un error de ejecución")
    abrir.close()

