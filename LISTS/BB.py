# ЧЕТНЫЕ ЭЛЕМЕНТЫ [СРЕЗЫ]
print(
    ' '.join(map(str, [x for x in map(int, input().split()) if x % 2 == 0]))
)