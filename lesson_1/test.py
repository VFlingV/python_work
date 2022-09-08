import random
n = int(input('N = '))
num = []
result = []
nums = [random.randint(-n, n) for _ in range(n)]
with open('file.txt', 'r', encoding='utf-8') as f:
    for i in f:
        num.append(int(i[0])) # оптимизировать
b = (num[:len(nums)])
for i in range(len(nums)):
    try:
        print(f'{nums[b[i]]} = {nums[b[i +1]]} ')
        a = nums[b[i]] * nums[b[i+1]]
        result.append(a)
    except IndexError:
        result.append('*')
print(result)

