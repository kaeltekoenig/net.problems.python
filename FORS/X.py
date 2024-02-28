N = int(input())

sides = 0
flipsides = 0


for side in range(N+1):
    for flipside in range(side, N+1):
        sides += side
        flipsides += flipside

print(sides + flipsides)