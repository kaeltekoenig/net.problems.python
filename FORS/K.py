n = int(input())

for i in range(n):
    print('+___', end='')
    if i != n-1:
        print(' ', end ='')
print()
for i in range(n):
    print(f'|{i+1} /', end='')
    if i != n-1:
        print(' ', end ='')
print()
for i in range(n):
    print('|__\\', end='')
    if i != n-1:
        print(' ', end ='')
print()
for i in range(n):
    print('|   ', end='')
    if i != n-1:
        print(' ', end ='')

