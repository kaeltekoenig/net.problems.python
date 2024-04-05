def reverse():
    q = int(input())
    if not q:
        print(0)
    else:
        reverse()
        print(q)

reverse()