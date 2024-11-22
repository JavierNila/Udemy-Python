class Vaca:

    def __init__(self,nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice muu")

class Oveja:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice bee")

vaca1 = Vaca('Aurora')
oveja1 = Oveja('Nube')

'''vaca1.hablar()
oveja1.hablar()'''

animales = [vaca1,oveja1]

'''for animal in animales:
    animal.hablar()'''


def animal_habla(animal):
    animal.hablar()

animal_habla(vaca1)
animal_habla(oveja1)

print("\n")

palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

for largo in [palabra,lista,tupla]:
    print(len(largo))

print("\n")

class Mago():
    def atacar(self):
        print("Ataque mágico")


class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")


class Samurai():
    def atacar(self):
        print("Ataque con katana")


arquero = Arquero()
mago = Mago()
samurai = Samurai()

personajes = [arquero, mago, samurai]
for ataque in personajes:
    ataque.atacar()

print("\n")

class Mago():
    def defender(self):
        print("Escudo mágico")


class Arquero():
    def defender(self):
        print("Esconderse")


class Samurai():
    def defender(self):
        print("Bloqueo")


def personaje_defender(personaje):
    personaje.defender()

