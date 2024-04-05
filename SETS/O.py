access = {}

for _ in range(int(input())):
    s = input().split()
    access[s[0]] = s[1:]


reductions = {'read': 'R',
              'write': 'W',
              'execute': 'X'}

for _ in range(int(input())):
    s = input().split()
    if reductions.get(s[0]) in access[s[1]]:
        print('OK')
    else:
        print('Access denied')

