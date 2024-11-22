import re

texto = "Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online"

patron = 'ayuda'

#busqueda = re.search(patron, texto)
busqueda = re.findall(patron, texto)
print(busqueda)
'''print(busqueda.span())
print(busqueda.end())'''
print(len(busqueda))

for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span())


texto = "llama al 564-525-6588 ya mismo"

#patron = r'\d\d\d-\d\d\d-\d\d\d\d'
#patron = r'\d{3}-\d{3}-\d{4}'
patron = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

resultado = re.search(patron, texto)

print(resultado)
print(resultado.group(1))

'''clave = input("Clave: ")

patron = r'\D{1}\w{7}'

chequear = re.search(patron, clave)

print(chequear)'''

texto = "No atendemos los lunes por la tarde"

#buscar = re.search(r'lunes|martes', texto)
#buscar = re.search(r'....demos...', texto)
#buscar = re.search(r'^\D', texto)
#buscar = re.search(r'\D$', texto)
#buscar = re.findall(r'[^\s]', texto)
buscar = re.findall(r'[^\s]+', texto)

print(' '.join(buscar))

print("\n")

def verificar_email(email):
    patron = r'@\w+\.com'
    verificar = re.search(patron, email)
    if verificar:
        print("Ok")
    else:
        print("La dirección de email es incorrecta")

print("\n")

def verificar_saludo(frase):
    patron = r'Hola'
    verificar = re.search(patron, frase)
    if verificar:
        print("Ok")
    else:
        print("No has saludado")

print("\n")

def verificar_cp(cp):
    patron = r'\w\w\d\d\d\d'
    verificar = re.search(patron, cp)
    if verificar:
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")