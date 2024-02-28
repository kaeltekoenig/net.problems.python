array = list(map(int, input().split()))
array = list(array[len(array)//2:] + array[:len(array)//2] 
             if len(array) % 2 == 0
             else array[(len(array)+1)//2:] + array[len(array)//2:len(array)//2+1] + array[:len(array)//2])

print(*array)