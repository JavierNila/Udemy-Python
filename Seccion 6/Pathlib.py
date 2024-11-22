from pathlib import Path, PureWindowsPath

carpeta = Path('C:/Users/SPARTAN PC/Documents/PYTHON/Seccion 6/Prueba.txt')

#El PureWindowsPath cambia la ruta a como se ve en windows de cualquier otro sistema operativo
ruta_windows = PureWindowsPath(carpeta)

'''if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("Genial, existe")'''

print(ruta_windows)