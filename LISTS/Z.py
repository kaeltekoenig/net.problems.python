coordinates = []
isBeaten = False

for i in range(8):
    coordinates.append(list(map(int, input().split())))
# print()

for i in range(7):
    x1, y1 = coordinates[i]
    # print(x1, y1)
    for j in range(i+1, 8):
        x2, y2 = coordinates[j]
        if (
            x2 == x1 or y2 == y1
            ) or (
            x2 == x1+1 and y2 == y1+1
            ) or (
            x2 == x1-1 and y2 == y1-1
            ) or (
            x2 == x1-1 and y2 == y1+1
            ) or (
            x2 == x1+1 and y2 == y1-1):
            isBeaten = True
            break

if isBeaten:
    print('YES')
else:
    print('NO')





# x1 = int(input())
# y1 = int(input())

# for i in range(7):
#     x2 = int(input())
#     y2 = int(input())
#     if (
#         x2 == x1 or y2 == y1
#         ) or (
#         x2 == x1+1 and y2 == y1+1
#     ) or (
#         x2 == x1-1 and y2 == y1-1
#     ):
#         print('YES')
#     else:
#         print('NO')



