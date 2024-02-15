K = int(input())
P = int(input())
S = int(input())

new_price = K + K * P * 10 ** -2
print(int(S // new_price))