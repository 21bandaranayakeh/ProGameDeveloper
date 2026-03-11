a = str(input('Please enter a string.   '))

a = a.lower()

b = ''
l = []
count = 0
count2 = 0


for i in a:
    l.append(i)

for i in range(len(l)):
    if l[i] == ' ':
        count += 1
        if l[i+1] == l[0]:
            count2 += 1

if count == count2:
    print('Your string is a tautogram.   ')
else:
    print('Your string is not a tautogram.   ')