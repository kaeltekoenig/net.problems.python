my_list = list(map(int, input().split()))

i = 0
while i < len(my_list) and my_list[i] < 1:
    i += 1

print(i)