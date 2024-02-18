name_1 = input()
name_2 = input()
name_3 = input()
N = int(input())

if N % 3 == 1:
    print(name_1)
elif N % 3 == 2:
    print(name_2)
else:
    print(name_3)