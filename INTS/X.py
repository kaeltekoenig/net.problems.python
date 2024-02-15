# Электронные часы - 3

x1 = 12
y1 = 34

a1 = 10
b1 = 0

x2 = 2
y2 = 34


time_passed = (x2 * 60 + y2) - (x1 * 60 + y1)
start = a1 * 60 + b1
end = (start + 2 * time_passed) % (60 * 24)
result = end // 60, end % 60
print(end // 60, end % 60)