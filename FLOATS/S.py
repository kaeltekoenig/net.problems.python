# n = int(input())
# a = int(input())
n = 3
a = 2

sum_ = 0


for i in range(n+1, 0, -1):
    current = a * i
    sum_ += current
    sum_ **= 0.5
print(sum_)