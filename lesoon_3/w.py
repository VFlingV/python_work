result = [2, 3, 4, 5, 2, 2, 5]
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