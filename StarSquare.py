a = int(input('Please enter how many rows you want.  '))

b = a - 1

for i in range(a):
    print('*',end=' ')
print()
for i in range(b-1):
    print('*',end=' ')
    for i in range(a - 2):
        print(' ',end=' ')
    print('*')

for i in range(a):
    print('*',end=' ')

