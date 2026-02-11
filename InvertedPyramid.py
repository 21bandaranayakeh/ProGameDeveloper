a = int(input('Please enter the amount of rows you want.  '))

b = 0

c = a

for i in range(a):
    for k in range(b):
        print(' ',end='')
    for j in range(c):
        print('*',end=' ')
    print()
    b += 1
    c -= 1