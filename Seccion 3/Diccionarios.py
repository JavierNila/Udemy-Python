diccionario = {'c1':'valor1','c2':'valor2'}
print(type(diccionario))
print(diccionario)

resultado = diccionario['c2']
print(resultado)

cliente = {'nombre':'Javier','apellido':'Arreguin','edad':21,'peso':80,'talla':1.85}
consulta = cliente["apellido"]
print(consulta)

dic = {'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200}}
print(dic['c3']['s2'])

ejemplo = {'c1':['a','b','c'],'c2':['d','e','f']}
print(ejemplo['c2'][1].upper())

dic2 = {1:'a',2:'b'}
print(dic2)

dic2[3] = 'c'
print(dic2)

dic2[2] = 'B'
print(dic2)

print(dic2.keys())
print(dic2.values())
print(dic2.items())