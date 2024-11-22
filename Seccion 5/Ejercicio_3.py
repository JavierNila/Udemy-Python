def ceros_consecutivos(*args):
    for i in range(len(args) - 1):
        if args[i] == 0 and args[i + 1] == 0:
            return True
    return False

numero = ceros_consecutivos(1,2,3,4,5,0,0,8,0)
print(numero)


