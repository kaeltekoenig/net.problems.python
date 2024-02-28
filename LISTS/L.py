# _input = '0 1 2 3 4'
# my_list = list(map(int, _input.split()))

my_list = list(map(int, input().split()))
minimal = float('inf')

for elem in my_list:
    if elem % 2 != 0 and elem < minimal:
        minimal = elem
if minimal == float('inf'):
    minimal = 0

print(minimal)
