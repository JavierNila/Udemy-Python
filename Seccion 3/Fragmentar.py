texto = "ABCDEFGHIJKLM"
#Los dos puntos es para indicar hasta que indice abarcar pero no incluyendo el mismo
fragmento = texto[2:10]
print(fragmento)

texto = "ABCDEFGHIJKLM"
#Si solamente dejo los dos puntos despues del indice en donde quiero empezar a contar, tomara todos los valores restantes
fragmento = texto[2:]
print(fragmento)

texto = "ABCDEFGHIJKLM"
#Si se hace lo contrario dejando los dos puntos y despues un indice, se tomaran todos hasta el indice indicado pero sin tomar ese
fragmento = texto[:5]
print(fragmento)

texto = "ABCDEFGHIJKLM"
#Se añaden otros dos puntos lo cual indica cuandos caracteres se van a ir extrayendo
fragmento = texto[2:10:3]
print(fragmento)

texto = "ABCDEFGHIJKLM"
#Si se ponen vacios los dos primeros dos puntos se tomara toda la cadena extrayendo el indice indicado
#Lo mismo pasara con los numeros negativos pero de derecha a izquierda
fragmento = texto[::3]
print(fragmento)