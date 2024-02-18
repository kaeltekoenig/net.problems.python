a = int(input())
b = int(input())
c = int(input())

if a >= b:
    max_1 = a
else:
    max_1 = b

if max_1 >= c:
    max_2 = max_1
else:
    max_2 = c

print(max_2)