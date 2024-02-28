array = list(map(int, input().split()))
k = int(input())


print(' '.join(map(str, array[-k:]+array[:-k])))