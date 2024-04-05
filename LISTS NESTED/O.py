def unfold_list(lst):
    for rw in lst:
        print(''.join(map(lambda el: str(el).rjust(4), rw)))


n, m = 5, 6
array = [[0 if r == c else 1 if r > c else 2 for c in range(m)] for r in range(n)]


unfold_list(array)