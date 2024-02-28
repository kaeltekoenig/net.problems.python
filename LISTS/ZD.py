array = list(map(int, input().split()))
array[1::2] = array[1::2][::-1]
print(*array)