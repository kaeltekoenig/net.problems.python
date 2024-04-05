def max_digit(n):
    global max_digit_value
    while n > 0:
        m = n % 10
        if m > max_digit_value:
            max_digit_value = m
        n //= 10



max_digit_value = 0
max_digit(321)
print(max_digit_value)
max_digit(179)
print(max_digit_value)