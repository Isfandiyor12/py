a = int(input())
fl = True
out = a
while fl:
    a -= 2
    if a > 0:
        out *= a
    else:
        fl = False
print(out)