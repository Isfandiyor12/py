a = input().lower()
b = input().lower()
k = 1
for i in a:
    if i in b:
        print(f'{k} встречается в строке поиска: {b[:b.index(i)] + b[b.index(i)].upper() + b[b.index(i) + 1:]}')
    k += 1
