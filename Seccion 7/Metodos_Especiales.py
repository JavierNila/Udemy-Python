mi_lista = [1,1,1,1,1,1,1]
print(mi_lista)

class Objeto:
    pass

mi_objeto = Objeto()
print(mi_objeto)

class CD:

    def __init__(self,autor,titulo,canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self):
        return f"Album: {self.titulo} de {self.autor}"

    def __len__(self):
        return self.canciones

    def __del__(self):
        print("Se ha eliminado el CD")

mi_cd = CD('Pink Floyd','The Wall',24)
print(mi_cd)
print(len(mi_cd))

del mi_cd

print("\n")

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __str__(self):
        return f'"{self.titulo}", de {self.autor}'

print("\n")

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __len__(self):
        return int(self.cantidad_paginas)

print("\n")

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __del__(self):
        print("Libro eliminado")