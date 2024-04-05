colors_ann = set()
colors_boris = set()

n, m = map(int, input().split())
for _ in range(n):
    colors_ann.add(int(input()))
for _ in range(m):
    colors_boris.add(int(input()))


print(len(colors_ann & colors_boris))
print(*(colors_ann & colors_boris))

print(len(colors_ann - colors_boris))
print(*colors_ann - colors_boris)

print(len(colors_boris - colors_ann))
print(*colors_boris - colors_ann)