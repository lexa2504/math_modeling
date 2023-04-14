import numpy as np
print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0")
print('Введите значение переменной a=')
a=float(input())
if a == 0:
    a=1
    print("a не должно быть = 0, поэтому по умолчанию будет = 1")

print('Введите значение переменной b=')
b=float(input())
print('Введите значение переменной c=')
c=float(input())

discriminant = (b**2)-(4*a*c)
print("Discr =", discriminant)

if discriminant > 0:
    x1 = (-b + np.sqrt(discriminant)) / (2 * a)
    x2 = (-b - np.sqrt(discriminant)) / (2 * a)
    print("x1 =", x1, "x2 =", x2)
elif discriminant == 0:
    x = (-b / (2 * a))
    print("x =", x) 
else:
    print("Корней нет")   

    

