total = 50

for num in range(total + 1):
    print(f'|{num:>{len(str(total))}}|{num ** 2:>{len(str(total ** 2))}}|{num ** 3:>{len(str(total ** 3))}}|')
