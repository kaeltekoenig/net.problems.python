my_list = list(map(int, input().split()))

index = 0

while index < len(my_list)-1 and (my_list[index] * my_list[index+1]) < 0:
    index += 1


if index < len(my_list)-1:
    print(my_list[index], my_list[index+1])
else:
    print()