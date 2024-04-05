array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in array:
    for col in row:
        print(col, end=' ')
    print()
print()
# 1 2 3 
# 4 5 6 
# 7 8 9 

for row in array:
    print(' '.join(map(str, row)))
print()
# 1 2 3 
# 4 5 6 
# 7 8 9 

#####

array = [[121, 2, 91], [24, 75, 6], [7000, 8, 79]]
width = 4

for row in array:
    for col in row:
        col = str(col)
        col += ' '*(width - len(col))
        print(col, end=' ')
    print()
print()
# 121  2    91   
# 24   75   6    
# 7000 8    79 

for row in array:
    for col in row:
        col = str(col)
        print(col.rjust(width), end=' ')
    print()
#  121    2   91 
#   24   75    6 
# 7000    8   79 