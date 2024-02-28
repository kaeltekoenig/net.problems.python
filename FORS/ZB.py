N = int(input()) - 1
x1 = 0
y1 = 0
x2 = 0
y2 = 1


for step in range(N):
    dx = x2 - x1
    dy = y2 - y1
    x2 += dy
    y2 -= dx
print(x2, y2)

# print(dx)
# print(dy)