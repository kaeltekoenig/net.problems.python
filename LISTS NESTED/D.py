def unfold_list(lst):
    for rw in lst:
        print(''.join(map(lambda el: str(el).rjust(4), rw)))


n, m = 5, 6

array = [[c + r for c in range(0, m*5, 5)] for r in range(n)]


unfold_list(array)
