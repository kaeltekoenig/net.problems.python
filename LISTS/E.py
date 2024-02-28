# my_list = list(map(int, input().split()))

# i = 0
# while i < len(my_list) and my_list[i] < 1:
#     i += 1

# if i > len(my_list)-1:
#     print(-1)
# else:
#     print(i)
    


# 2
my_list = list(map(int, input().split()))

my_list.append(999)
i = 0

while i < len(my_list) and my_list[i] < 1:
    i += 1

if i == len(my_list)-1:
    print(-1)
else:
    print(i)

my_list.pop()