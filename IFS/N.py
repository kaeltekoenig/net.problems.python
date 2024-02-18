n = int(input())

if n % 10 == 1:
    cows = 'корова'
elif 1 < n % 10 < 5:
    cows = 'коровы'
else:
    cows = 'коров'
    
print(n, cows)