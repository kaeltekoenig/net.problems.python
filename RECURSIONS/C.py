# МИНИМАЛЬНАЯ ЦИФРА ЧИСЛА
def min_digit(n):
    if n // 10 == 0:
        return min(n, 9)
    else:
        return min(n % 10, min_digit(n // 10))
    

print(min_digit(991))