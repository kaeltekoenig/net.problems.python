number = 2002

f_part = number // 100
digits = number % 100 // 10
units = number % 10


print(
f_part // (units * 10 + digits)
)



# f_part = number // 100
# s_part = number % 100
# print(str(f_part) == str(s_part).zfill(2)[::-1])