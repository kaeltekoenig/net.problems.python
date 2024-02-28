# n = int(input())
# total = 1

# for i in range(1, n + 1):
#     total *= i

# print(total)


####

n = 10 ** 3
total = 1



while n > 1:
    total *= n
    n -= 1


print('READY!')
print(total.bit_length() == 18488885)