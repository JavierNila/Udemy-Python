def letras_unicas(palabra):
    pal = sorted(set(palabra))
    return pal

prueba = letras_unicas("entretenido")
print(prueba)
