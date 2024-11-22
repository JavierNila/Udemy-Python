def cambiar_letras(tipo):

    def mayuscula(texto):
        print(texto.upper())

    def minuscula(texto):
        print(texto.lower())

    if tipo == 'may':
        return mayuscula
    elif tipo == 'min':
        return minuscula


#operacion = cambiar_letras('may')
#operacion('palabra')

'''mi_funcion = mayuscula

mi_funcion('python')
'''


'''def una_funcion(funcion):
    return funcion

una_funcion(mayuscula('probando'))'''

def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print('hola')
        funcion(palabra)
        print('adios')
    return otra_funcion

@decorar_saludo
def mayusculas(texto):
    print(texto.upper())

@decorar_saludo
def minusculas(texto):
    print(texto.lower())

mayusculas('python')
#minusculas('PYTHON')

'''mayuscula_decorada = decorar_saludo(mayusculas)
mayuscula_decorada('fede')'''

