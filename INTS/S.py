n = int(input())
start = 9 * 60
current_minutes = start + n * 45 + 10 * ((n - 1) // 2) + 5 * (n - 1)

# print(
#     f'После {n} уроков прошло {n * 45} минут.\n'
#     f'Время: {current_minutes // 60}:{str(current_minutes % 60).zfill(2)}'
#     )

print(current_minutes // 60, current_minutes % 60)
