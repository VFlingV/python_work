
def txt(t):
    t_2 = t.split()
    result = []
    for i in range(len(t_2)):
        if not t_2[i].count('а'):
            result.append(t_2[i])
            print(t_2[i])

    print(result)
text = input('введите текст = ')
txt(text)
