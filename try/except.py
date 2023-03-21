# coding=utf-8
a = int(input('Ввести делимое:'))
b = int(input('Ввести делитель:'))
try:
   x = a / b
   print(x)
except ZeroDivisionError:
   print("Ошибка! Деление на 0 не возможно")
finally:
   print("Финальная попытка")
   b = int(input("Введи делитель:"))
   x = a / b
   print (x)