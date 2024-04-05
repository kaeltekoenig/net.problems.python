cities = {}

for _ in range(int(input())):
    s = input().strip().split()
    cities[s[0]] = s[1:]

for _ in range(int(input())):
    q = input()
    for cou, cts in cities.items():
        if q in cts:
            print(cou)
