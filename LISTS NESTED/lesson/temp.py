def create_matrix(rows, cols, vl=0):
    return [[vl for col in range(cols)] for row in range(rows)]


def unfold_mult_array(lst):
    for i in lst:
        for j in i:
            print(j, end=' ')
        print()



# unfold_mult_array(create_matrix(5, 5, 0))
        
array = []

for row in range(3):
    nested = []
    for col in range(3):
        nested.append(col)
    array.append(nested)


unfold_mult_array(array)