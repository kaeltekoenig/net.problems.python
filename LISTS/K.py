# _input = '1 2 2 3 3 3'
# my_list = list(map(int, _input.split()))

my_list = list(map(int, input().split()))
new_list = my_list[:]

new_list.append('temp')
for index, elem in enumerate(my_list):
    if elem in my_list[index+1:]:
        new_list.remove(elem)

new_list.pop()
print(len(new_list))