# Количество нулей в десятичной записи
print(sum(z == '0' for x in range(1, int(input())+1) for z in str(x)))