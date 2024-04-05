def unfold_list(lst):
    for rw in lst:
        print(''.join(map(lambda el: str(el).rjust(4), rw)))


n, m = 5, 6
array = [[0 if r % 2 == 1 and c % 2 == 1 else 1 for c in range(m)] for r in range(n)]


unfold_list(array)