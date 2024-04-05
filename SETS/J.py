calender, parties = map(int, input().split())

strikes = set()
saturdays = set(range(6, calender + 1, 7))
sundays = set(range(7, calender + 1, 7))

for par in range(parties):
    start, freq = map(int, input().split())
    strikes |= set(range(start, calender + 1, freq))

strikes -= saturdays | sundays
print(len(strikes))