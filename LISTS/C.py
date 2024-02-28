my_list = list(map(int, input().split()))

prev = my_list[0]

for elem in my_list:
    if elem > prev:
        print(elem, end=' ')
    prev = elem