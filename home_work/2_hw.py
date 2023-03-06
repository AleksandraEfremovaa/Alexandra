#задача 1
def task_1(a: int = 5, b: float = 3.2, c: str = 'hello',
           f: list = [1, 4, 8, 9], k: bool = True):
   return type(a), type(b), type(c), type(f), type(k)

print(task_1())

#2 var
def task_1():
    a: int = 5
    b: float = 3.2
    c: str = 'hello'
    f: list = [1, 4, 8, 9]
    k: bool = True
    return print(type(a), type(b), type(c), type(f), type(k))


print(task_1())

# Задача 2
def task_2():
    a = [1, 2, 3, 5, 8, 12, 21]
    return a[0:3]
print(task_2(), "- последовательность натуральных чисел")

# Задача 3
def task_3(a: int):
    return a**2
print(task_3(5))
