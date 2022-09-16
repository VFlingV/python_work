import random
b = int(input('b = '))
i = 0
result = []
while i < b:
    a = random.randint(0, 10)
    i += 1
    result.append(a)
print(result)

b = result[::-1]
result_2 = []
i = 0
while i < len(result):
    c = result[i] * b[i]
    result_2.append(c)
    result.pop()
    b.pop()
    i += 1
print(result_2)