from math import *
a = float(input("Введите значение для a: "))
b = float(input("Введите значение для b: "))
c = float(input("Введите значение для c: "))
A = degrees(acos((b**2 + c**2 - a**2)/(2*b*c)))
B = degrees(acos((c**2 + a**2 - b**2)/(2*c*a)))
C = degrees(acos((a**2 + b**2 - c**2)/(2*a*b)))
print(A, B, C)
