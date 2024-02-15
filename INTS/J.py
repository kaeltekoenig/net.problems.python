# Стоимость покупки
# Пирожок в столовой стоит 

a = int(input())
b = int(input())
n = int(input())

kopeks = (a * 100 + b) * n

print(kopeks // 100, kopeks % 100)