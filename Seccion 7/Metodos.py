class Pajaro:

    alas = True

    def __init__(self,color,especie):
        self.color = color
        self.especie = especie

    def piar(self):
        #print('pio, mi color es {}'.format(self.color))
        print(f"pio, mi color es {self.color}")

    def volar(self,metros):
        print(f"El pajaro ha volado {metros} metros")

piolin = Pajaro('amarillo','canario')
piolin.piar()
piolin.volar(50)
#print(f"El pajaro es un {piolin.especie} de color {piolin.color}")

print("\n")

class Perro:
    def ladrar(self):
        print("Guau!")

perro = Perro()
perro.ladrar()

print("\n")

class Mago:
    def lanzar_hechizo(self):
        print("¡Abracadabra!")

merlin = Mago()
merlin.lanzar_hechizo()

print("\n")

class Alarma:
    def postergar(self,cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")

alarma = Alarma()
alarma.postergar(5)

