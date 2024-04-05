def median(a, b, c):
    return sum([a, b, c]) - min(a, b, c) - max(a, b, c)

a = int(input())
b = int(input())
c = int(input())

print(median(a, b, c))