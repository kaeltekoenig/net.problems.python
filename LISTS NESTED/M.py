def unfold_list(lst):
    for rw in lst:
        print(''.join(map(lambda el: str(el).rjust(4), rw)))


n, m = 10, 10
array = [[1 if (c + r) % 4 == 1 else 0 for c in range(m)] for r in range(n)]


unfold_list(array)