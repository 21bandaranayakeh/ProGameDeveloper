from random import randint

l = [['P', 2, 3, 4, 5, 6, 7, 'L1', 9, 10], [11, 12, 'S2', 14, 15, 16, 17, 'L2', 19, 20], ['S1', 22, 23, 24, 'L3', 26, 27, 28, 'S4', 30], [31, 32, 33, 'L4', 35, 36, 37, 38, 39, 40], ['L5', 42, 43, 44, 45, 'S3', 47, 48, 'S6', 50], [51, 52, 53, 'L6', 55, 56, 57, 58, 59, 'S5'], [61, 62, 63, 64, 65, 66, 67, 'L7', 69, 70], ['S8', 72, 73, 74, 75, 76, 77, 78, 'S7', 80], [81, 'S10', 83, 84, 85, 86, 'L8', 88, 'L9', 90], [91, 92, 93, 94, 95, 'L10', 97, 'S9', 99, 100]]


# snakes = [12, 19, 27, 34, 49, 52, 65, 76, 83, 94]

# ladders = [3, 18, 22, 36, 47, 54, 69, 73, 87, 92]
dict1 = {
    1:0,
    2:1,
    3:2,
    4:3,
    5:4,
    6:5,
    7:6,
    8:7,
    9:8,
    10:9,
    11:0,
    12:1,
    13:2,
    14:3,
    15:4,
    16:5,
    17:6,
    18:7,
    19:8,
    20:9,
    21:0,
    22:1,
    23:2,
    24:3,
    25:4,
    26:5,
    27:6,
    28:7,
    29:8,
    30:9,
    31:0,
    32:1,
    33:2,
    34:3,
    35:4,
    36:5,
    37:6,
    38:7,
    39:8,
    40:9,
    41:0,
    42:1,
    43:2,
    44:3,
    45:4,
    46:5,
    47:6,
    48:7,
    49:8,
    50:9,
    51:0,
    52:1,
    53:2,
    54:3,
    55:4,
    56:5,
    57:6,
    58:7,
    59:8,
    60:9,
    61:0,
    62:1,
    63:2,
    64:3,
    65:4,
    66:5,
    67:6,
    68:7,
    69:8,
    70:9,
    71:0,
    72:1,
    73:2,
    74:3,
    75:4,
    76:5,
    77:6,
    78:7,
    79:8,
    80:9,
    81:0,
    82:1,
    83:2,
    84:3,
    85:4,
    86:5,
    87:6,
    88:7,
    89:8,
    90:9,
    91:0,
    92:1,
    93:2,
    94:3,
    95:4,
    96:5,
    97:6,
    98:7,
    99:8,
    100:9,
}
# a = 0
p = 1

r = 0

i = 0

j = 0

flag = 0

sublist_max = 10

def show_grid():
    for i in range(9, -1, -1):
        print()
        for j in l[i]:
            print(j,end=' ')

while True:
    print()
    num = int(input('Enter a number.'))
    # num = randint(1, 6)
    print('You rolled a {}'.format(num))
    if p + num <= sublist_max:
        l[r][dict1[p + num]] = 'P'
        l[r][dict1[p]] = p
        p = p + num
    elif p + num > sublist_max:
        r += 1
        l[r-1][dict1[p]] = p
        l[r][dict1[p + num]] = 'P'
        p = p + num
        sublist_max += 10
    print(p + num)
    if p + num == 8:
        l[0][7] = 'L1'
        l[1][7] = 'P'
        print('Ladder')
    elif p + num == 25:
        l[2][4] = 'L3'
        l[3][3] = 'P'
        print('Ladder')
    elif p + num == 41:
        l[4][0] = 'L5'
        l[5][3] = 'P'
        print('Ladder')
    elif p + num == 68:
        l[6][7] = 'L7'
        l[8][6] = 'P'
        print('Ladder')
    elif p + num == 89:
        l[8][8] = 'L9'
        l[9][5] = 'P'
        print('Ladder')
    elif p + num == 21:
        l[2][0] = 'S1'
        l[1][2] = 'P'
        print('Snake')
    elif p + num == 46:
        l[4][5] = 'S3'
        l[2][8] = 'P'
        print('Snake')
    elif p + num == 60:
        l[5][9] = 'S5'
        l[4][8] = 'P'
        print('Snake')
    elif p + num == 79:
        l[7][8] = 'S7'
        l[7][0] = 'P'
        print('Snake')
    elif p + num == 98:
        l[9][7] = 'S9'
        l[8][1] = 'P'
        print('Snake')
    elif p + num >= 100:
        print()
        print('You Win!')
        break
    i += 1
    j += 1
    show_grid()

    







































# while a != '-1':
#     a = input('Please type anything to roll (-1 to stop).   ')
#     num = randint(1, 6)
#     print('You rolled {}'.format(num))
#     s += num
#     for i in snakes:
#         if s == i:
#             s -= 10
#             print('snake, down 10 spots')
#     for i in ladders:
#         if s == i:
#             s += 10
#             print('ladder, up 10 spots')
#     if s >= 100:
#         print('You win')
#         break
#     print('Spot {}'.format(s))