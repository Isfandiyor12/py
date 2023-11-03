a = input()
b = input()
out = ''
for i in a:
    if i in b and out.count(i) + 1 <= b.count(i):
        out += i
print(out)