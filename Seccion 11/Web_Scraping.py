import bs4
import requests

# Enlace de la página a requisar
resultado = requests.get('https://www.escueladirecta.com/courses/')

# Siempre usar esto para que el contenido de la página lo cambia a un lxml
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

# print(sopa.select('title')[0].getText())
# parrafo_especial = sopa.select('a')[3].getText()

'''columna_lateral = sopa.select('.widget-content span')
for p in columna_lateral:
    print(p.getText())'''

# Para descargar una imagen
'''imagenes = sopa.select('.course-box-image')[0]['src']
print(imagenes)

imagen_curso = requests.get(imagenes)
# print(imagen_curso.content)

f = open('mi_imagen.jpg', 'wb')
f.write(imagen_curso.content)
f.close()'''


