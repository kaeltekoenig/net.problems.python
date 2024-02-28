my_list = list(map(int, input().split()))
# _input = '6 5 4 2 1'
# my_list = list(map(int, _input.split()))

key = int(input())
minimum = float('inf')

for elem in my_list:
    if abs(key - elem) < minimum:
        number = elem
        minimum = abs(key - elem)

# print(minimum)
print(number)