n = 10
m = 10

array = [[int((x + z) % 4 == 1) for z in range(m)] for x in range(n)]


def unfold_mult_list(lst):
    for row in lst:
        for col in row:
            print(col, end=' ')
        print()

unfold_mult_list(array)