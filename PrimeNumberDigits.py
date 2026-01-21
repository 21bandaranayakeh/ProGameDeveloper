a = input('Please enter a number. ')

num = 0
count = 0

for i in a:
    s = int(i)
    num += s

for i in range(1, num+1):
    if num % i == 0:
        count += 1

if count == 2:
    print('The sum of the digits is {}'.format(num))
    print('The sum of the digits of your number is a prime number.')
else:
    print('The sum of the digits is {}'.format(num))
    print('The sum of the digits in your number is not a prime number.')