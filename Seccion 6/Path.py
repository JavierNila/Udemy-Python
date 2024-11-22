from pathlib import Path

base = Path.home()
print(base)

#Path construye a partir de una lista de objetos alguna ruta de acceso
'''guia = Path(base,"Europa","España",Path("Barcelona","Sagrada_Familia.txt"))'''

'''guia2 = guia.with_name("La_Pedrera.txt")'''

'''guia = Path(Path.home(),"Europa")'''
#Usando un solo asterisco engloba a todos los archivos dentro del directorio y usando dos ateriscos barra asterisco
# es todos los directorios y sus subdirectorios con archivos
'''for txt in Path(guia).glob(("**/*.txt")):
    print(txt)'''

#Relative to es para un nuevo objeto path en relacion con el argumento determinado o apartir de
guia = Path("Europa","España","Barcelona","Sagrada_Familia.txt")
en_europa = guia.relative_to(Path("Europa"))
en_espania = guia.relative_to(Path("Europa","España"))

print(en_europa)
print(en_espania)

print("\n")


print("\n")


print("\n")

