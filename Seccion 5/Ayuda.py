#Esta seccion es mas que nada para tomar en cuenta la documentacion oficial
dic = {'Clave1':100,'Clave2':500}

a = dic.popitem()
print(a)
print(dic)

print("\n")

texto = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#".lstrip(",:_%#")

print(texto)

print("\n")

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]\

añadir = frutas.insert(3,'naranja')
print(añadir)

print("\n")

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)


