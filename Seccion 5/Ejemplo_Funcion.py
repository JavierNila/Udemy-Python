precios_cafe = [('Capuchino',1.5),('Expresso',2.5),('Moka',1.9)]

def cafe_mas_caro(lista_precios):
    precio_mayor = 0
    cafe_mas_caro = ''

    for cafe,precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass
    return (cafe_mas_caro,precio_mayor)

print(cafe_mas_caro(precios_cafe))

cafe, precio = cafe_mas_caro(precios_cafe)
print(f"El cafe mas caro es {cafe} cuyo precio es {precio}")

print("\n")

#Se puede reutilizar el mismo codigo para hacer pruebas diferentes
precios_cafe = [("capuchino", 1.5), ("Expresso", 1.2), ("Moka", 1.9)]
precios_jugos = [("manzana", 2.5), ("mango", 2.2), ("piña", 2.9)]

def producto_mas_caro(lista_precios):
    precio_mayor = 0
    cafe_mas_caro = ""

    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass
    return (cafe_mas_caro, precio_mayor)

cafe, precio_cafe = producto_mas_caro(precios_cafe)
jugo, precio_jugo = producto_mas_caro(precios_jugos)

print(f"El cafe mas caro es {cafe}. Cuyo precio es: ${precio_cafe}")
print(f"El jugo mas caro es {jugo}. Cuyo precio es: ${precio_jugo}")
