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
        num.append(int(i[0])) # оптимизировать//// не придумаk как
b = (num[:len(nums)])
print(b)
print(nums)

for i in range(len(nums)):
    try:
        print(f'{nums[b[i]]} * {nums[b[i +1]]} ')
        a = nums[b[i]] * nums[b[i+1]]
        result.append(a)
    except IndexError:
        if b[i] == len(nums):
            result.append('*')
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

import random
n = int(input('N = '))
num = []
result = []
nums = [random.randint(-n, n) for _ in range(n)]

with open('file.txt', 'r', encoding='utf-8') as f:
    for i in f:
        num.append(int(i[0])) # оптимизировать
b = (num[:len(nums)])
print(b)
print(nums)

for i in range(len(nums)):
    try:
        print(f'{nums[b[i]]} * {nums[b[i +1]]} ')
        a = nums[b[i]] * nums[b[i+1]]
        result.append(a)
    except IndexError:
        if b[i] == len(nums):
            result.append(nums[b[i]])
        elif b[i] > len(nums):
            result.append('*')
print(result)




'''