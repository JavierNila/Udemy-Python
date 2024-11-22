class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

mi_pajaro = Pajaro('negro', 'Tucan')

print(f"Mi pajaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}")

print(Pajaro.alas)
print(mi_pajaro.alas)

print("\n")

class Casa:
    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos

casa_blanca = Casa('blanco', 4)
print(f"El color de la casa es {casa_blanca.color} y tiene {casa_blanca.cantidad_pisos} pisos")

print("\n")

class Cubo:
    caras = 6

    def __init__(self, color):
        self.color = color

cubo_rojo = Cubo('rojo')
print(f"El cubo es de color {cubo_rojo.color} y tiene {cubo_rojo.caras} caras")

print("\n")

class Personaje:
    real = False

    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad

harry_potter = Personaje('Humano', True, 17)

print(f"Harry Potter es {harry_potter.especie}, tiene {harry_potter.edad} años, pero no es real ¿o si? {harry_potter.real} y es magico ¿verdad? {harry_potter.magico}")