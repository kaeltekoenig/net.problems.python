N = int(input())
A = int(input())
B = int(input())

buses = 0
taxi = 0

# print(f'Изначально точное поедет на автобусе: {N // 50}')


buses += N // 50
N %= 50


# print(f'Общее количество оставшихся человек для рассадки: {N}')
# print(
#     f'Стоимость на автобусе для {N} человек: {A * ((N - 1) // 50 + 1)}\n'
#     f'Стоимость на автобусе для {N} человек: {B * ((N - 1) // 4 + 1)}'
# )


# Рассаживаем оставшихся
if A * ((N - 1) // 50 + 1) < B * ((N - 1) // 4 + 1):
    buses += (N - 1) // 50 + 1
else:
    taxi += (N - 1) // 4 + 1

print(buses, taxi)