#Con el AND ambas deben de ser iguales
mi_bool = (4 < 5) and (5 == 2+3)
print(mi_bool)

mi_bool = (55 == 55) and ('perro' == 'perro')
print(mi_bool)

#Con el OR una de las dos debe ser igual
mi_bool = 10 == 10 or 3 == 3
print(mi_bool)

mi_bool = 1 == 10 or 3 == 6
print(mi_bool)

texto = "esta frase es breve"
mi_bool = ('frase' in texto) and ('breve' in texto)
print(mi_bool)

texto = "esta frase es breve"
mi_bool = ('frase' in texto) and ('python' in texto)
print(mi_bool)

texto = "esta frase es breve"
mi_bool = ('frase' in texto) or ('breve' in texto)
print(mi_bool)

mi_bool = not ( 'a' != 'a')
print(mi_bool)