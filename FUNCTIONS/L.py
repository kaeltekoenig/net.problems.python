# ПРОИЗВЕДЕНИЕ ЦИФР
def product_of_digits(n):
    mult = 1
    while n > 0:
        mult *= n % 10
        n //= 10

    return mult


print(product_of_digits(int(input())))