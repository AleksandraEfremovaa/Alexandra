def num(x, y):
    return print(max(x, y))
num(4, 17)

#2 task

def num1(a, b):
    if max(a, b) - min(a, b) == 135:
        return print('yes')
    else:
        return print('no')
num1(135, 0)

def num2(c):
    if c in (12, 1, 2):
        return print('winter')
    elif c in range(3,6):
        return print('spring')
    elif c in range(6,9):
        return print('summer')
    else:
        return print('autumn')
num2(10)

def lists(list1:list):
    count = 0
    for i in range(len(list1)):
        if list1[i] > 0:
            count = count + 1

    return print(count)

lists([1, 2, 3, 4, -5])

def num3(a, b, c):
    if a > 10 and b > 10 and c > 10:
        return print('yes')
    else:
        return print('no')
num3(15, 11, 0)

def num4(a, b):
    return print(a * 29 * 12 + b * 29)
num4(4, 8)


