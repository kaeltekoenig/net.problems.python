n = 5
m = 6

array = [[int(x % 2 + z % 2 != 0 ) for z in range(1, m+1)] for x in range(1, n+1)]


def unfold_mult_list(lst):
    for row in lst:
        for col in row:
            print(col, end=' ')
        print()

unfold_mult_list(array)