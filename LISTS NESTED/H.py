def unfold_list(lst):
    for rw in lst:
        print(''.join(map(lambda el: str(el).rjust(4), rw)))


n, m = 5, 6

array = [[min(r, c) for c in range(m-1, -1, -1)] for r in range(n-1, -1, -1)]


unfold_list(array)
