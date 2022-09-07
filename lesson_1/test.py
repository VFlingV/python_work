result = []
g = [1, 3, 1, 3, 7, 2]
for i in g:
    try:
        print(g[i])

    except IndexError:
        pass
