#Pone el texto en mayusculas
texto = "Este es el texto de Federico"
resultado = texto.upper()
print(resultado)

#Aqui en minusculas
texto = "Este es el texto de Federico"
resultado = texto.lower()
print(resultado)

#Aqui lo corta
texto = "Este es el texto de Federico"
resultado = texto.split()
print(resultado)

#Aqui lo corta respecto al parametro dado, como un punto de referencia sin considerar al mismo
texto = "Este es el texto de Federico"
resultado = texto.split("t")
print(resultado)

#Aqui se unen considerando el espacio
a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d])
print(e)

#Este metodo es para encontrar el caracter o la palabra que deseas
texto = "Este es el texto de Federico"
resultado = texto.find("texto")
print(resultado)

#Este metodo es para reemplazar tanto palabras completas o una sola dentro de el texto
texto = "Este es el texto de Federico"
resultado = texto.replace("t","m")
print(resultado)

resultado = texto.replace("Federico","Javier")
print(resultado)