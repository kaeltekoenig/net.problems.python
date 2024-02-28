import math

g = 9.81

v = 500
alpha = 0.2

x = (v ** 2) * math.sin(2 * alpha) / g
print(x)