numbers = set(range(1, int(input()) + 1))

while True:
    words = input()
    if words == 'HELP':
        break
    called = set(words.split())
    answer = input()
    if answer == 'NO':
        numbers -= called
    elif answer == 'YES':
        numbers = called - numbers


print(*sorted(numbers))

