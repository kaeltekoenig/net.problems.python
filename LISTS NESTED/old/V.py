n = 6
m = 9



array = [[2 - int(x == 1 or z == 1 or x == (n-2) or z == (m-2)) 
          if int(x != 0 and z != 0 and x != (n-1) and z != (m-1)) else 0 
          for z in range(m)]
          for x in range(n)]


for row in array:
    for col in row:
        print(str(col).rjust(2), end=' ')
    print()


