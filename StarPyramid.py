a = int(input('Please enter the amount of rows you want.  '))

b = a - 1

c = 1

for i in range(a):
    for i in range(b):
        print(' ',end='')
    for j in range(c):
        print('*',end=' ')
    print()
    b -= 1
    c += 1