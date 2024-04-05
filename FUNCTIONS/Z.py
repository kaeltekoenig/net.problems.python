prev = 0

def read():
    global prev
    n = int(input())
    isEqual = n == prev
    prev = n
    return isEqual


print(read())
print(prev)
print(read())
print(prev)
print(read())
print(prev)
print(read())
print(prev)