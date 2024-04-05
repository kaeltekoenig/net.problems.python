total_sum = 0

def sum_list(a):
    global total_sum
    total_sum += sum(a)


total_sum = 0
sum_list([1, 2, 3])
print(total_sum)
sum_list([1, 7, 9])
print(total_sum)