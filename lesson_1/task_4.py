'''
Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
Позиции хранятся в файле file.txt в одной строке одно число.
'''
import random

n = int(input('N = '))
nums = [random.randint(-n, n) for _ in range(-n, n + 1)]
print(nums)
num = []
b = 0
with open ('file.txt', 'r', encoding='utf-8') as f:
    for i in f:
        num.append(i[0])
print(num)

for i in range(len(nums)):
    b = nums[i] * num[i]
print(b)