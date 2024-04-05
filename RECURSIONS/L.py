def print_numbers(a, b):
    a, b = min(a, b), max(a, b)
    if b == a:
        print(a)
    else:
        print_numbers(a, b - 1)
        print(b)

print_numbers(7, 4)