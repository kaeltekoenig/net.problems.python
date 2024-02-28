angle = int(input())

hour = angle // 30
minutes = (angle % 30) / 30 * 360

print(minutes)