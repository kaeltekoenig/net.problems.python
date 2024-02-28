P = int(input())
X = int(input())
Y = int(input())

kopeks = X * 100 + Y
income = kopeks + kopeks * P // 100

print(
    income // 100, income % 100
)