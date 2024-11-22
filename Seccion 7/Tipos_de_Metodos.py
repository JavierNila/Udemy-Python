class Pajaro:

    alas = True

    def __init__(self,color,especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print(f"pio")

    def volar(self,metros):
        print(f"El pajaro ha volado {metros} metros")
        self.piar()

    def pintar_negro(self):
        self.color = 'negro'
        print(f"Ahora el pajaro es {self.color}")

    #Este tipo de metodos no pueden acceder a los de instancia pero si a los de clase
    @classmethod
    def poner_huevos(cls,cantidad):
        print(f"Puso {cantidad} huevos")
        cls.alas = False
        print(Pajaro.alas)

    #No pueden modificar el estado de una instancia ni los atributos de la clase
    @staticmethod
    def mirar():
        print("El pajaro mira")

#piolin.pintar_negro()
#piolin.volar(50)
#piolin.alas = False

Pajaro.poner_huevos(3)
Pajaro.mirar()

print("\n")

class Mascota:
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")

print("\n")

class Jugador:
    vivo = False

    @classmethod
    def revivir(cls):
        cls.vivo = True
        print(Jugador.vivo)

print("\n")

class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        self.cantidad_flechas = self.cantidad_flechas - 1
        print(f"Cantidad de flechas: {self.cantidad_flechas}")

flecha = Personaje(6)
flecha.lanzar_flecha()


