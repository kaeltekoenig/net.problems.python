# Счастливые билеты
print(sum(sum(map(int, x[:2])) == sum(map(int, x[2:])) for x in [str(a).zfill(4) for a in range(10**6)]))