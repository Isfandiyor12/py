s = input()
l = len(s)
out = ''
for i in range(1, l + 1):
    if l % i == 0:
        out += s[i - 1]
print(out)