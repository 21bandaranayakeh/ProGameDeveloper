l = []
gr = -999999
a = 0
k = int(input('Please enter a number. '))


while a != -1:
    a = int(input('Please enter a list of numbers (-1 to stop)  '))
    if a != -1:
        l.append(a)


for j in range(k - 1):
    for i in l:
        if i > gr:
            gr = i
    l.remove(gr)
    gr = -999999

for i in l:
    if i > gr:
        gr = i


print('The number which was the {}th greatest was {}. '.format(k, gr))