'''
Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
-
'''
n = 0
a = int(input('введите целое число = '))
my_list = []
result = []
for i in range(a):
    my_list.append(i+1)
b = my_list[0]
while n < a:
    b = b * my_list[n]
    result.append(b)
    n += 1
print(result)




