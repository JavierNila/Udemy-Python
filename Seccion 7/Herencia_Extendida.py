class Animal:

    def __init__(self,edad,color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("Este animal emite un sonido")

class Pajaro(Animal):

    def __init__(self,edad,color,altura_vuelo):
        super().__init__(edad,color)
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print("pio")

    def volar(self,metros):
        print(f"El pajaro vuela {metros} metros")

piolin = Pajaro(3,'amarillo',60)
mi_animal = Animal(5,'negro')

'''piolin.nacer()
piolin.hablar()
piolin.volar(100)'''

#Herencia Multiple

class Padre:
    def hablar(self):
        print("Hola")

class Madre:
    def reir(self):
        print("ja ja")

    def hablar(self):
        print("que tal")

#Siempre dependera del orden en el que se heredan
'''class Hijo(Padre, Madre):
    pass'''
class Hijo(Madre, Padre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()
mi_nieto.hablar()

print(Nieto.__mro__)

print("\n")

class Padre():
    def trabajar(self):
        print("Trabajando en el Hospital")

    def reir(self):
        print("Ja ja ja!")


class Madre():
    def trabajar(self):
        print("Trabajando en la Fiscalía")

class Hija(Madre, Padre):
    pass

print("\n")

class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")

class Ornitorrinco(Pez,Reptil,Ave,Mamifero,Vertebrado):
    pass

print(Ornitorrinco.__mro__)

print("\n")

class Padre():
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"

    def reir(self):
        return "Jajaja"

    def hobby(self):
        return "Pinto madera en mi tiempo libre"

    def caminar(self):
        return "Caminando con pasos largos y rápidos"

class Hijo(Padre):
    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"





