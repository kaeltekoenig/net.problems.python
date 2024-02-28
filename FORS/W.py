n = int(input())
output = 0
fact = 1

for i in range(1, n+1):
    fact *= i 
    output += fact

print(output)

