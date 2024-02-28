n = int(input())
x = float(input())


exp = 1
sum_ = 1
factorial = 1

for i in range(1, n+2):
    exp *= x
    factorial *= i
    # print(f'Индекс: {i}')
    # print(f'Текущее x в степени: {exp}')
    # print(f'Текущий факториал: {factorial}')
    # print(f'Сумма: {sum_}')
    # print()
    if i % 2 == 0:
        if i % 4 == 0:
            sum_ += exp / factorial
            # print(f'Текущее x в степени: {exp}')
            # print(f'Текущий факториал: {factorial}')
            # print(f'Сумма: {sum_}')
        else:
            sum_ -= exp / factorial
            # print(f'Текущее x в степени: {exp}')
            # print(f'Текущий факториал: {factorial}')
            # print(f'Сумма: {sum_}')
    
    

print(sum_)
        
