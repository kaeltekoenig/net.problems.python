a = int(input())
b = int(input())

for i in range(a, b+1):
    thousands = i // 1000
    hundreds = i // 100 % 10
    tens = i % 100 // 10
    units = i % 10
    if (
        thousands == hundreds == tens) or (
        thousands == hundreds == units) or (
        thousands == tens == units) or (
        hundreds == tens == units
        ):
        print(i)

