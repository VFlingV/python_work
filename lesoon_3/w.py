a = [2, 3, 4, 5, 2]


b = a[::-1]
print(a)
print(b)
result_1 = []

try:
    result_1 = [a[i] * b[i] and a.pop(i) and b.pop(i) for i in range(len(a))]

except IndexError:
    print(result_1)