n = int(input())
x = float(input())

formula = 0
order = 0

for monomial in range(n+1, 0, -1):
    order += 1
    a = float(input())
    if monomial == 1:
        formula += a
    elif order == 2:
        formula += a
        formula *= x
    else:
        formula += a * x
    
    
print(formula)