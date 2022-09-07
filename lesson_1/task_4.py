'''
Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
Позиции хранятся в файле file.txt в одной строке одно число.
'''
import random
n = int(input('N = '))
nums = [random.randint(-n, n) for _ in range(n)]
num = []

with open('file.txt', 'r', encoding='utf-8') as f:
    for i in f:
        num.append(int(i[0]))
print(nums)
print(num[:len(nums)])



result = [nums[i] * nums[i] for i in (num[:len(nums)]) if i < len(nums)]
print(result)


'''
result = [int(num[i]) * nums[i] for i in range(len(nums))]
print(result)


for i in range(len(nums)):
    b = int(nums[i]) * num[i]
    result.append(b)
print(result)
'''