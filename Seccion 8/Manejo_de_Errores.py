def suma():
    n1 = int(input("numero 1: "))
    n2 = int(input("numero 2: "))
    #print(n1 + n2)
    #print("Gracias por sumar" + n1)

'''try:
    #Codigo que queremos probar
    suma()
except:
    #Codigo a ejecutar si hay un error
    print("Algo no ha salido bien")
else:
    #Codigo a ejecutar si no hay un error
    print("Hiciste todo bien")
finally:
    #Codigo que se va a ejecutar de todos modos
    print("Eso fue todo")'''


'''try:
    #Codigo que queremos probar
    suma()
except TypeError:
    #Codigo a ejecutar si hay un error
    print("Estas intentando concatenar tipos distintos")
except ValueError:
    print("Ese no es un numero")
else:
    #Codigo a ejecutar si no hay un error
    print("Hiciste todo bien")
finally:
    #Codigo que se va a ejecutar de todos modos
    print("Eso fue todo")'''

def pedir_numero():
    while True:
        try:
            numero = int(input("Dame un numero: "))
        except:
            print("Ese no es un numero")
        else:
            print(f"Ingresaste el numero: {numero}")
            break

    print("Gracias")

pedir_numero()

print("\n")

"""
Ejemplo de resolución:

def nombre_funcion(argumento):
    try:
        {Lo que haría la función habitualmente}
    except:
        {Excepción}
    else:
        ... etc.
"""


def suma(num1, num2):
    try:
        print(num1 + num2)
    except:
        print("Error inesperado")

print("\n")

"""
Ejemplo de resolución:

def nombre_funcion(argumento):
    try:
        {Lo que haría la función habitualmente}
    except:
        {Excepción}
    else:
        ... etc.
"""


def cociente(num1, num2):
    try:
        print(num1 / num2)
    except TypeError:
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")

print("\n")

"""
Ejemplo de resolución:

def nombre_funcion(argumento):
    try:
        {Lo que haría la función habitualmente}
    except:
        {Excepción}
    else:
        ... etc.
"""


def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo)
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except:
        print("Error desconocido")
    else:
        print("Abriendo exitosamente")
    finally:
        print("Finalizando ejecución")

