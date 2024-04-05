n = 5
col = 6

n = [[i * j for j in range(col)] for i in range(row)]

for i_row in array:
    for i_col in i_row:
        print(str(i_col).rjust(2), end=' ')
    print()
