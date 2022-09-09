a = [2, 3, 4, 5, 2, 2, 5]
b = a[::-1]
result = []
i = 0
while i < len(a):
    c = a[i] * b[i]
    result.append(c)
    a.pop()
    b.pop()
    i += 1
print(result)

'''
for i in range(len(a)):
    c = int(a[i]) * int(b[i])
    result.append(c)

print(result)

for i in range(len(a)):
    c = a[i] * a[len(a)-1:]
    result.append(c)
    a.pop()
print(c)
'''

