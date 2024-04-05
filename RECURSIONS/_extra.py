# СУММА ДВУХ ЧИСЕЛ
def summ(a, b):
    if a == 0:
        return b
    else:
        return summ(a - 1, b + 1)
    
# СУММА ЦИФР
def sdigit(n):
    if n == 0:
        return 0
    return n % 10 + sdigit(n // 10)


# ПРОВЕРКА НА СТЕПЕНЬ ДВОЙКИ
def istwobase(n):
    if n == 1:
        return True
    return n % 2 == 0 and istwobase(n // 2)


# ПАЛИНДРОМ
def ispal(s):
    if len(s) <= 1:
        return True
    return s[0] == s[1] and ispal(s[1:-1])


# РАСПЕЧАТЬ ЦИФРЫ ЧИСЛА ЧЕРЕЗ ПРОБЕЛ
def p(n):
    if n < 10:
        print(n, end=' ')
    else:
        p(n // 10)
        print(n % 10, end=' ')


# ВОЗВЕДЕНИЕ В СТЕПЕНЬ ЗА O(LOG(N))
def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n - 1) if n % 2 == 1 else power(a, n // 2) ** 2


print(power(2, 100))

