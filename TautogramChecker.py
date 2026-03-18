a = 0
c = 0
l = []

while a != '-1':
    a = str(input('Please enter a string.   '))
    c += 1

    a = a.lower()
    if a != '-1':
        l.append(a)



n = 0
b = ''
count = 0
count2 = 0
count3 = 0

for i in l:
    for j in range(len(l[n])):
        if l[n][j] == ' ':
            count += 1
            if l[n][j+1] == l[n][0]:
                count2 += 1

    if count == count2:
        count3 += 1
    count = 0
    count2 = 0
    n += 1

print('You have entered a total of {} tautograms.   '.format(count3))
