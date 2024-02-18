a = int(input())
b = int(input())
c = int(input())

u = int(input())
v = int(input())
x = int(input())
# print()


if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a

# print(a, b, c)
# print()

if u > v:
    u, v = v, u
if v > x:
    v, x = x, v
if u > v:
    u, v = v, u

# print(u, v, x)
# print()

print(
(a // u) * (b // v) * (c // x)
)