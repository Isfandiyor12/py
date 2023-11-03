fl = True
while fl:
    s = input()
    if len(s) != 0:
        fl = False
        if s == 'STOP':
            print('Program interrupted by user')
            s = s.rsplit(' ', '_')
        elif s[0] > 'a':
            print('Too early in the dictionary. Try again!')
            fl = True
        else:
            s = s.center(30 + len(s), '_')
            print(s)
