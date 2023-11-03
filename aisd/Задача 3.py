a = int(input())
out = a
for i in range(a // 2):
    a -= 2
    if a > 0:
        out *= a
print(out)