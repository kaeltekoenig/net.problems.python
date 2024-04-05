customers = {}

with open('input.txt', 'r') as f:
    while True:
        s = f.readline().rstrip().split()

        if not s:
            break

        if s[0] not in customers:
            customers[s[0]] = {}
        if s[1] not in customers[s[0]]:
             customers[s[0]][s[1]] = 0

        customers[s[0]][s[1]] += int(s[2])

for k, v in dict(sorted(customers.items())).items():
    print(k)
    for f, s in sorted(v.items()):
        print(f, s)

