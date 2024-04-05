n = 5
m = 5

array = [[abs(z-x) for z in range(m-1, -1, -1)] for x in range(n)]


def unfold_mult_list(lst):
    for row in lst:
        for col in row:
            print(col, end=' ')
        print()

unfold_mult_list(array)