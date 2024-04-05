def hanoicyc(n, s, f):
    if n > 0:
        t = 6 - f - s
        if s == 3 and f == 1:
            print(n, s, f)
        else:
            hanoicyc(n - 1, s, f)
            print(n, s, t)
            hanoicyc(n - 1, f, s)
            print(n, t, f)
            hanoicyc(n - 1, s, f)

hanoicyc(3, 1, 3)    






# def move(n, start, finish):
#     if n > 0:
#         tmp = 6 - start - finish
#         if (finish - start) % 3 == 1:
#             move(n - 1, start, tmp) 
#             print(n, start, finish) 
#             move(n - 1, tmp, finish) 
#         else:
#             move(n - 1, start, finish) 
#             print(n, start, tmp) 
#             move(n - 1, finish, start) 
#             print(n, tmp, finish) 
#             move(n - 1, start, finish) 
# move(3, 1, 3)
