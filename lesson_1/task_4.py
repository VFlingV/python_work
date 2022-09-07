'''
Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
Позиции хранятся в файле file.txt в одной строке одно число.
'''
import random
n = int(input('N = '))
num = []
result = []
nums = [random.randint(-n, n) for _ in range(n)]

with open('file.txt', 'r', encoding='utf-8') as f:
    for i in f:
        num.append(int(i[0])) # оптимизировать
print('a =', nums)
b = (num[:len(nums)])
print('b = ', b)
try:
    for i in b:
        result.append(nums[i])
    print(result)
except IndexError:
    print(result)




"""
result = [nums[i] * nums[i] for i in b]
print(result)
"""

'''
result = [int(num[i]) * nums[i] for i in range(len(nums))]
print(result)


for i in range(len(nums)):
    b = int(nums[i]) * num[i]
    result.append(b)
print(result)
'''