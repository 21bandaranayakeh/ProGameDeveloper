
a = 0
gr = -999999
l = []

while a != -1:
    a = int(input('Please enter some numbers (-1 to end).  '))
    if a != -1:
        l.append(a)

for i in l:
    if i > gr:
        gr = i
l.remove(gr)
gr = -999999

for i in l:
    if i > gr:
        gr = i
l.remove(gr)
gr = -999999

for i in l:
    if i > gr:
        gr = i
l.remove(gr)
gr = -999999

for i in l:
    if i > gr:
       gr = i

print('The fourth largest number is {}'.format(gr))