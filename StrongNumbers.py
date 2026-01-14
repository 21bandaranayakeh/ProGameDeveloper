a = input('Please enter an integer (whole number): ')

f = 0
l = []

for i in a:
    s = int(i)
    num = 1
    for i in range(1, s + 1):
        num = i * num
    l.append(num)

for i in range(len(l)):
    f += l[i]

s = int(a)

if f == s:
    print('Your number is a strong number.')
else:
    print('Your number is not a strong number.')

# num = 1

# for i in range(1, a + 1):
#     num = i * num

# print(num)

# num = 0

# for i in range(1, a+1):
#     num = num + i

# print(num)
    