number = int(input())
order = len(str(number)) - 1

for i in range(9, 0, -1):
    number += i * 10 ** order
    new_order = len(str(number)) - 1
    if new_order > order or number % 3 != 0:
        number -= i * 10 ** order
    else:
        print(number)
        break