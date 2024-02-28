h = float(input())
m = float(input())
s = float(input())

hour_vel = (360 / 12) * h
min_vel = (m * 30) / 60
sec_vel = (s * 30) / 3600

print(
    hour_vel + min_vel + sec_vel
)