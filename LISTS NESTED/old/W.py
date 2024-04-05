n = 8

# int(not(2 < z < 5 or 2 < x < 5))
array = [[3 - 
          - int(not((x == 3 or x == 5) and z < 3))
          for z in range(n)] for x in range(n)]



for row in array:
    for col in row:
        print(col, end=' ')
    print()