def read():
    nums = set()
    while True:
        n = int(input())

        if n in nums:
            return n
        nums.add(n)

print(read())