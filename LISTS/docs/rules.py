# ### 1
# N = int(input('Введите количество элементов для списка: '))

# my_list = [0] * N


# for i in range(N):
#     my_list[i] = int(input('Введите данные: '))

# print(my_list)


# ### 2
# my_list = input().split()

# for i in range(len(my_list)):
#     my_list[i] = int(my_list[i])

# print(my_list)


### 3

# my_list = map(int, input().split())
# print(my_list)
# # <map object at 0x0000024DB48A7820>
# # Возвращает map object, поэтому надо обернуть в список дополнительно

my_list = [54, 8, 4, 65, 7, 54, 862]
# my_list = list(map(int, input().split()))
print(my_list)

# print(' '.join(my_list))
# TypeError: sequence item 0: expected str instance, int found

print(' '.join(map(str, my_list))) # надо привести к строке


watermelon_masses = [2, 5, 1, 7, 8, 4, 3]

m = watermelon_masses[0]
for elem in watermelon_masses:
    if elem > m:
        m = elem

print(m) # 8


key = 4

watermelon_masses[i] == key