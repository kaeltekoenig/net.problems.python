numbers = set(range(1, int(input()) + 1))

while True:
    words = input()
    if words == 'HELP':
        break
    called = set(map(int, words.split()))
    if len(called) <= len(numbers) // 2:
        print('NO')
        numbers -= called
    else:
        print('YES')
        numbers = numbers & called

print(*sorted(numbers))

