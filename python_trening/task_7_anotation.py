a: int = 5
b: str = 'строка'
c: list = [1, 2]

def indent(s: str, width: int) -> str:
    return ' ' * (max(0, width - len(s))) + s

print(indent('123', 123))

def ff(s: str) ->int:
    return len(s)

print(ff(''))

def fff(a: list, b: list) -> int:
    return max(len(a), len(b))
print(fff([2, 5, 7], [3, 4, 8, 7, 9, 0]))