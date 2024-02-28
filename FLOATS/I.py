P = int(input())
X = int(input())
Y = int(input())
K = int(input())

kopeks = X * 100 + Y
income = kopeks

while K > 0:
    kopeks = X * 100 + Y
    income = int(kopeks + kopeks * P / 100)
    X = income // 100
    Y = income % 100
    K -= 1


print(
    X, Y
)