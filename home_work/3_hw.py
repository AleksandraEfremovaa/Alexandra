a = int(input('Введите число а:'))
b = int(input('Введите число b:'))
if a > b:
    print('a > b')
elif a == b:
    print('a = b')
else:
    print('b > a')

# 2 задача

c = int(input('Введите число c:'))
n = int(input('Введите число n:'))
a = c - n
b = n - c
if c - n == 135 or n - c == 135:
    print('Yes')
else:
    print('No')

# 3 задача

month = int(input('Введите номер месяца:'))
if month in range(9, 10, 11):
    print('autumn')
elif month in range(3, 4, 5):
    print('spring')
elif month in range(6, 7, 8):
    print('summer')
else:
    print('winter')

# 4 задача

a, b, c = int(input('1 number:')), int(input('2 number:')), int(input('3 number:'))
if a >= int(10) and b >= int(10) and c >= int(10):
    print('Yes')
else:
    print('No')



