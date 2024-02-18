N = int(input())
M = int(input())
x = int(input()) # Рассотяние до длинного бортика
y = int(input()) # Рассотяние до короткого бортика


# Пусть М - длинный бортик
if N > M:
    N, M = M, N
print(min(min(x, N - x), min(y, M - y)))
# Проплыть нужно параллельно
# if (M - y) < (N - x):
#     print(M - y)
# else:
#     print(N - x)

# # Второе решение
# if N > M:
#     print(min(min(x, N - x), min(y, M - y)))
# else:
#     print(min(min(x, M - x), min(y, N - y)))