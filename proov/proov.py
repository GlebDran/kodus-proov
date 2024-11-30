from math import *

chislo1 = int(input("введите первое число: "))
chislo2 = int(input("введите второе число: "))
summa = chislo1 + chislo2
print(f"сумма чисел: {summa}")

print("\n-----")

chislo = int(input("введите число: "))
if chislo % 2 == 0:
    print("Число четное.")
else:
    print("Число нечетное.")

print("\n-----")

stroka = input("введите строку: ")
print(f"обратный порядок: {stroka[::-1]}")

print("\n-----")

dlina = int(input("введите длину прямоугольника:" ))
shirina = int(input("введите ширину прямоугольника:" ))
ploshad = dlina*shirina
print(f"площадь прямоугольника: {ploshad}")

print("\n-----")

celsium = float(input("введите температуру в цельсиях: "))
farengeit = celsium * 9/5 + 32
print(f"температура в градусах Фаренгейта: {farengeit}")