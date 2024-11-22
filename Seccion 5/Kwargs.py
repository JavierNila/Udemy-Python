def suma(**kwargs):

    total = 0

    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor

    return total

print(suma(x=3, y=5, z=2))

print("\n")

def prueba(num1, num2, *args, **kwargs):

    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")

    for arg in args:
        print(f"Arg = {arg}")

    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")


args = [100,200,300,400]
kwargs = {'x':'uno','y':'dos','z':'tres'}

prueba(15,50,*args,**kwargs)

print("\n")

def cantidad_atributos(**kwargs):
    return len(kwargs)

print("\n")

def lista_atributos(**kwargs):
    return list(kwargs.values())

print("\n")

def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")


describir_persona('María',color_ojos= 'azules',color_pelo='rubio' )




