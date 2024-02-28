angle = float(input())
# angle = 31.05

# hour = int(angle // 30)
# minutes = 2 * int(angle % 30)
# seconds = (angle - int(angle)) / 60 * 360 * 2

total_seconds = int(angle / (1/120))
hour = total_seconds // 3600
minutes = int(total_seconds % 3600) // 60
seconds = int(total_seconds % 3600) % 60


print(hour, minutes, seconds)