n = int(input())
total = 1


for i in range(1, n+1):
    current = (1 / (2 * i + 1))
    if i % 2 != 0:
        current *= -1
    total += current


print(4 * total)





# num = n
# for i in range(n):
#     num += i
#     num *= -1
#     print(num)