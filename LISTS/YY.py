# КУЗНЕЧИКИ [СРЕЗЫ]
array = list(map(int, input().split()))

for i in range(int(input())):
    array.insert(-array[-1], array.pop())

print(array)