my_list = list(map(int, input().split()))
# my_list = [1, 0, 1, 0, 1]


total = 0
for index, value in enumerate(my_list):
    if index != len(my_list)-1:
        if value > my_list[index-1] + my_list[index+1]:
            total += 1

print(total)