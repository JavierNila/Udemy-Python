def devolver_distintos(num1,num2,num3):
    suma = num1 + num2 + num3
    if suma > 15:
        return max(num1,num2,num3)
    elif suma < 10:
        return min(num1,num2,num3)
    elif suma in range(10,16):
        return suma // 2

print(devolver_distintos(5,5,8))
print(devolver_distintos(1,2,6))
print(devolver_distintos(4,5,5))