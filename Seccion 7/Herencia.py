class Animal:

    def __init__(self,edad,color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")

class Pajaro(Animal):
    pass

piolin = Pajaro(2,'amarillo')
piolin.nacer()
print(piolin.color)
print(piolin.edad)

print("\n")

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Alumno(Persona):
    pass

print("\n")

class Mascota:
    def __init__(self,edad,nombre,cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas

class Perro(Mascota):
    pass

print("\n")

class Vehiculo:
    def acelerar(self):
        pass

    def frenar(self):
        pass

class Automovil(Vehiculo):
    pass