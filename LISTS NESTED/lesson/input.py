n, m = map(int, input().split())
a = [0] * n

for i in range(n):
    a[i] = list(map(int, input().split()))



n, m = map(int, input().split())
a = []

for i in range(n):
    a.append(list(map(int, input().split())))


###
# одномерный
array = [input() for i in range(int(input()))] 
print(array)


# двумерный
array = [list(map(int, input().split())) for i in range(int(input()))]  # на вход одно число int
print(array)

array = [list(map(int, input().split())) for i in range(int(input().split()[0]))]  # на вход два число в строку
print(array)