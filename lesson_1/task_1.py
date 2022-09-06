'''
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11
'''
import string

a = input('введите положительное число число = ')
n = 0
a = a.translate(str.maketrans('', '', string.punctuation))
if str.isdigit(a):
    for i in a:
        n += int(i)
    print(n)
else:
    print('некорректное значение')





"""
n = 0
for i in a:
     n += int(i)
print(n)
"""


