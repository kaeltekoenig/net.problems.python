import math
N = int(input())

total = [int(input()) for x in range(N)]
total_sum = 0
special = []

# total = [125, 50, 490, 215, 144, 320]

for el in total:
    if el > 50:
        special.append(el)


special = sorted(special[:len(special)//2])



new = []
for t in total:
    if not(t) in special:
        new.append(t)


for i in range(len(special)):
    special[i] *= 0.75


for s in special:
    new.append(s)

print(math.ceil(sum(new)))


