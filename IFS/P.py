n = int(input())


abon_max = n // 60
abon_10 = (n % 60) // 10
units = (n % 60) % 10

if abon_10 > 3:
    abon_max += 1 * (abon_10 // 3)
    abon_10 = 0
if units > 8:
    abon_10 += 1 * (units // 8)
    units = 0

print(units, abon_10, abon_max)
