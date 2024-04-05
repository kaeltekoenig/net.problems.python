def square_num(x):
    return x ** 2

# Лябмда-функция - без имени
# Формат: lambda аргументы: выражение
# Вызавается через переменную, которой присваивается:

square = lambda x: x ** 2
print(square(14))                           # 196



def fperimeter(a, b, c):
    return a + b + c

perimeter = lambda a, b, c: a + b + c
print(perimeter(9, 43, 2))                  # 54


# Можно без аргументов

wow = lambda: 'wow!'
print(wow())                                # wow!


# Условие


def define_number(num):
    return 'positive' if num > 0 else 'negative'

print(define_number(-21))               # negative

dfn_number = lambda num: 'positive' if num > 0 else 'negative'

print(dfn_number(78))                   # positive