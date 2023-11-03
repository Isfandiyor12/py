a = int(input())
b = int(input())
for i in range(a, b + 1):
    k = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            k = False
            break
    if k:
        print(i)