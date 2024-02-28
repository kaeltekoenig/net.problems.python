my_list = list(map(int, input().split()))

height = int(input())
index = 0
while index < len(my_list) and my_list[index] >= height:
    index += 1

print(index+1)
