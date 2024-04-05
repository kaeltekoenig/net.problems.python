votes = {}

with open('input.txt', 'r') as f:
    while True:
        s = f.readline().split()
        if s:
            m, v = s

            if m not in votes:
                votes[m] = 0
            votes[m] += int(v)
        else:
            break

votes = dict(sorted(votes.items()))

for c, v in votes.items():
    print(c, v)
