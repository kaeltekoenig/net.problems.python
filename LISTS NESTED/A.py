def unfold_list(lst):
    for rw in lst:
        print(''.join(map(lambda el: str(el).rjust(4), rw)))


n, m = 5, 6

array = [[r for c in range(m)] for r in range(n)]


unfold_list(array)
